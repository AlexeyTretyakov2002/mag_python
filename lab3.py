import sys, os, csv, random, shutil
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QAction
from PyQt5 import uic, QtWidgets

class MainWindow(QMainWindow):
    folderpath = ""
    instances = set()

    def __init__(self):
        super().__init__()

        # Загрузка формы из файла .ui
        uic.loadUi('mainwindow.ui', self)

        # Обработка нажатий на кнопки
        self.btn_task1.clicked.connect(self.task1)
        self.btn_task2.clicked.connect(self.task2)
        self.btn_task3.clicked.connect(self.task3)
        self.btn_task4.clicked.connect(self.task4)

    def get_next_instance(class_label, instances):        
        for instance in instances:
            instance = instance.split(";")
            if instance[2] == class_label:
                instances.pop()
                return instance[0]
            else:
                  return None

    def task1(self):
        self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите датасет')
        self.edt_task1.setText(self.folderpath)

    def task2(self):
        annotation_file = "annotation.csv"
        with open(annotation_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Absolute Path', 'Relative Path', 'Class Label'])
    
            for root, dirs, files in os.walk(self.folderpath):
                for file in files:
                    class_label = os.path.basename(root)
                    absolute_path = os.path.join(root, file)
                    relative_path = os.path.relpath(absolute_path, self.folderpath)
                    writer.writerow([absolute_path, relative_path, class_label])
        
        with open('annotation.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                self.instances.add(row[0])   
        self.edt_task2.setText("Сделано!")

    def task3(self):    
        with open('annotation.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
          
            if(not(os.path.exists("random_dataset"))):
                os.mkdir("random_dataset")
                
            for row in reader:
                row = row[0].split("\\")
                absolute_path = row[0]
                class_label = row[2]
                random_number = random.randint(0, 10000)
                file_name = f"{random_number}.txt"
                destination_path = os.path.join("random_dataset", file_name)
                shutil.copyfile(absolute_path, destination_path)
        self.edt_task3.setText("Выполняю!")

    def task4(self):
        for instance in self.instances:
            instance = instance.split("\\")
            if instance[1] == 'good':
                self.instances.pop()
                self.edt_review.clear()
                self.edt_review.appendPlainText(instance[0] + "\n" + instance[1] + "\n" + instance[2])
                break

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())