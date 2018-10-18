from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import os
import subprocess
import time
import tkinter as tk

CONFIG_FILE = 'config_demos.json'
SU_TITLE = 'Festival de Ingeniería y Ciencias 2018'
SU_TEXT = 'Demostraciones del Laboratorio de Inteligencia Computacional\n' \
          'Depto. de Ingeniería Civil Eléctrica, FCFM, Universidad de Chile'


class SuperInterface(object):

    def __init__(self, config_file):
        self.config_file = config_file
        self.demo_list, self.button_width, self.button_height, self.python_path, self.wait_seconds = self.read_config()
        self.process_list = []
        self.top = self.build_interface()

    def start(self):
        self.top.mainloop()

    def read_config(self):
        with open(self.config_file) as f:
            data = json.load(f)
        demo_list = data['demos']
        button_width = data['button_width']
        button_height = data['button_height']
        python_path = data['python_path']
        wait_seconds = data['wait_seconds_between_commands']
        return demo_list, button_width, button_height, python_path, wait_seconds

    def run_command(self, command_string_list):
        # my_env = os.environ.copy()
        for running_p in self.process_list:
            running_p.kill()
        self.process_list = []
        if len(command_string_list) > 1:
            wait = self.wait_seconds
        else:
            wait = 0
        for command_string in command_string_list:
            print("\nExecuting '%s'" % command_string)
            # command_list = command_string.split()
            # if command_list[0] == 'python':
            #     p = subprocess.Popen(command_list, env=my_env)
            # else:
            #     p = subprocess.Popen(command_list)
            # p = subprocess.Popen(command_string, shell=True)
            # command_string = 'bash -c "' + command_string + '"'
            command_string = command_string.replace("python", self.python_path)
            command_list = command_string.split()
            p = subprocess.Popen(command_list)
            print('Executed process with PID %d' % p.pid)
            self.process_list.append(p)
            time.sleep(wait)
        print(self.process_list)

    def build_interface(self):
        n_demos = len(self.demo_list)
        global_width = self.button_width + 2 * self.button_height
        global_height = (n_demos+1) * (self.button_height + 10) + 50
        top = tk.Tk()
        top.title(SU_TITLE)
        top.geometry('%dx%d' % (global_width, global_height))
        label = tk.Label(top, text=SU_TEXT)
        label.pack()
        for i in range(n_demos):
            demo_name = self.demo_list[i]['name']
            demo_command_list = self.demo_list[i]['command']
            print('Adding %s with command %s' % (demo_name, demo_command_list))
            this_button = tk.Button(top, text=demo_name, width=10,
                                    command=lambda d=demo_command_list: self.run_command(d))
            this_button.place(x=self.button_height, y=(i+1)*(self.button_height+10),
                              width=self.button_width, height=self.button_height)
        return top


if __name__ == '__main__':
    su = SuperInterface(CONFIG_FILE)
    su.start()
