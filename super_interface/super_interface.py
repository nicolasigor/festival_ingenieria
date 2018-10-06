from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import subprocess
import tkinter as tk

CONFIG_FILE = 'config_demos.json'
SU_TITLE = 'Demos interface'
SU_TEXT = 'Welcome to demos!'


class SuperInterface(object):

    def __init__(self, config_file):
        self.config_file = config_file
        self.demo_list, self.button_width, self.button_height = self.read_config()
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
        return demo_list, button_width, button_height

    def run_command(self, command_string):
        for running_p in self.process_list:
            running_p.kill()
            self.process_list.remove(running_p)
        print("Executing '%s'" % command_string)
        command_list = command_string.split()
        p = subprocess.Popen(command_list)
        # p = subprocess.Popen('exec '+command_string, shell=True)
        self.process_list.append(p)
        print(self.process_list)
        print('Executed process with PID %d\n' % p.pid)

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
            demo_command = self.demo_list[i]['command']
            print('Adding %s with command %s' % (demo_name, demo_command))
            this_button = tk.Button(top, text=demo_name, width=10,
                                    command=lambda d=demo_command: self.run_command(d))
            this_button.place(x=self.button_height, y=(i+1)*(self.button_height+10),
                              width=self.button_width, height=self.button_height)
        return top


if __name__ == '__main__':
    su = SuperInterface(CONFIG_FILE)
    su.start()
