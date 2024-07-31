import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from IPython.display import display
import ipywidgets as widgets
from ipywidgets import interact,HBox, VBox
import matplotlib.gridspec as gridspec
import json

def reset_answers():
    with open("answers.json", "w") as f:
        json.dump({}, f)

def exercise_example():
    mean = widgets.FloatText(
#         value='',
        placeholder=0.0,
        description='Probability:',
        disabled=False   
    )

    
    button = widgets.Button(description="Save your answer!", button_style="success")
    output = widgets.Output()
    
    display(mean)
    
    display(button, output)

    def on_button_clicked(b):
                    
        with output:
            print("Answer for the example exercise saved.")
            

    button.on_click(on_button_clicked)       
        
def exercise_1():
    mean = widgets.FloatText(
#         value='',
        placeholder=0.0,
        description='Mean:',
        disabled=False   
    )

    var = widgets.FloatText(
#         value='',
        placeholder=0.0,
        description='Variance:',
        disabled=False   
    )

    
    button = widgets.Button(description="Save your answer!", button_style="success")
    output = widgets.Output()
    
    display(mean)
    display(var)
#     display(cov)
    
    display(button, output)

    def on_button_clicked(b):
        
        with open("answers.json", "r") as f:
            source_dict = json.load(f)
            
        answer_dict = {
            "ex1": {
                "mean": mean.value,
                "var": var.value,
            }
        }
        
        source_dict.update(answer_dict)
        
        with open("answers.json", "w") as f:
            json.dump(source_dict, f)
            
        with output:
            print("Answer for exercise 1 saved.")
            

    button.on_click(on_button_clicked)

    
def exercise_2():
    hist = widgets.ToggleButtons(
        options=['left', 'center', 'right'],
        description='Your answer:',
        disabled=False,
        button_style='', # 'success', 'info', 'warning', 'danger' or ''
    )
    
    button = widgets.Button(description="Save your answer!", button_style="success")
    output = widgets.Output()
    
    display(hist)

    display(button, output)

    def on_button_clicked(b):
        
        with open("answers.json", "r") as f:
            source_dict = json.load(f)
            
        answer_dict = {
            "ex2": {
                "hist": hist.value
            }
        }
        
        source_dict.update(answer_dict)
        
        with open("answers.json", "w") as f:
            json.dump(source_dict, f)
            
        with output:
            print("Answer for exercise 2 saved.")
            

    button.on_click(on_button_clicked)
    
    
def exercise_3():
    sum_2_8 = widgets.FloatText(
#         value='',
        placeholder=0.0,
        description='P for sum=2|8',
        style = {'description_width': 'initial'},
        disabled=False   
    )

    sum_3_7 = widgets.FloatText(
#         value='',
        placeholder=0.0,
        description='P for sum=3|7:',
        style = {'description_width': 'initial'},
        disabled=False   
    )

    sum_4_6 = widgets.FloatText(
#         value='',
        placeholder=0.0,
        description='P for sum=4|6:',
        style = {'description_width': 'initial'},
        disabled=False   
    )
    
    sum_5 = widgets.FloatText(
#         value='',
        placeholder=0.0,
        description='P for sum=5:',
        style = {'description_width': 'initial'},
        disabled=False   
    )
    
    button = widgets.Button(description="Save your answer!", button_style="success")
    output = widgets.Output()
    
    display(sum_2_8)
    display(sum_3_7)
    display(sum_4_6)
    display(sum_5)
    
    display(button, output)

    def on_button_clicked(b):
        
        with open("answers.json", "r") as f:
            source_dict = json.load(f)
            
        answer_dict = {
            "ex3": {
                "sum_2_8": sum_2_8.value,
                "sum_3_7": sum_3_7.value,
                "sum_4_6": sum_4_6.value,
                "sum_5": sum_5.value
            }
        }
        
        source_dict.update(answer_dict)
        
        with open("answers.json", "w") as f:
            json.dump(source_dict, f)
            
        with output:
            print("Answer for exercise 3 saved.")
            

    button.on_click(on_button_clicked)

def exercise_4():
    mean = widgets.FloatText(
#         value='',
        placeholder=0.0,
        description='Mean:',
        disabled=False   
    )

    var = widgets.FloatText(
#         value='',
        placeholder=0.0,
        description='Variance:',
        disabled=False   
    )

    cov = widgets.FloatText(
#         value='',
        placeholder=0.0,
        description='Covariance:',
        disabled=False   
    )
    
    button = widgets.Button(description="Save your answer!", button_style="success")
    output = widgets.Output()
    
    display(mean)
    display(var)
    display(cov)
    
    display(button, output)

    def on_button_clicked(b):
        
        with open("answers.json", "r") as f:
            source_dict = json.load(f)
            
        answer_dict = {
            "ex4": {
                "mean": mean.value,
                "var": var.value,
                "cov": cov.value
            }
        }
        
        source_dict.update(answer_dict)
        
        with open("answers.json", "w") as f:
            json.dump(source_dict, f)
            
        with output:
            print("Answer for exercise 4 saved.")
            

    button.on_click(on_button_clicked)

    
def exercise_5():
    hist = widgets.ToggleButtons(
        options=['left', 'center', 'right'],
        description='Your answer:',
        disabled=False,
        button_style='', # 'success', 'info', 'warning', 'danger' or ''
    )
    
    button = widgets.Button(description="Save your answer!", button_style="success")
    output = widgets.Output()
    
    display(hist)

    display(button, output)

    def on_button_clicked(b):
        
        with open("answers.json", "r") as f:
            source_dict = json.load(f)
            
        answer_dict = {
            "ex5": {
                "hist": hist.value
            }
        }
        
        source_dict.update(answer_dict)
        
        with open("answers.json", "w") as f:
            json.dump(source_dict, f)
            
        with output:
            print("Answer for exercise 5 saved.")
            

    button.on_click(on_button_clicked)
    

def exercise_6():
    max_sum = widgets.IntSlider(
        value=2,
        min=2,
        max=12,
        step=1,
        description='Sum:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='d'
    )
    
    button = widgets.Button(description="Save your answer!", button_style="success")
    output = widgets.Output()
    
    display(max_sum)

    display(button, output)

    def on_button_clicked(b):
        
        with open("answers.json", "r") as f:
            source_dict = json.load(f)
            
        answer_dict = {
            "ex6": {
                "max_sum": max_sum.value
            }
        }
        
        source_dict.update(answer_dict)
        
        with open("answers.json", "w") as f:
            json.dump(source_dict, f)
            
        with output:
            print("Answer for exercise 6 saved.")
            

    button.on_click(on_button_clicked)
    
    
def exercise_7():
    hist = widgets.ToggleButtons(
        options=['left-most', 'left-center', 'right-center', 'right-most'],
        description='Your answer:',
        disabled=False,
        button_style='', # 'success', 'info', 'warning', 'danger' or ''
    )
    
    button = widgets.Button(description="Save your answer!", button_style="success")
    output = widgets.Output()
    
    display(hist)

    display(button, output)

    def on_button_clicked(b):
        
        with open("answers.json", "r") as f:
            source_dict = json.load(f)
            
        answer_dict = {
            "ex7": {
                "hist": hist.value
            }
        }
        
        source_dict.update(answer_dict)
        
        with open("answers.json", "w") as f:
            json.dump(source_dict, f)
            
        with output:
            print("Answer for exercise 7 saved.")
            

    button.on_click(on_button_clicked)
    
    
def exercise_8():
    hist = widgets.ToggleButtons(
        options=['left-most', 'left-center', 'right-center', 'right-most'],
        description='Your answer:',
        disabled=False,
        button_style='', # 'success', 'info', 'warning', 'danger' or ''
    )
    
    button = widgets.Button(description="Save your answer!", button_style="success")
    output = widgets.Output()
    
    display(hist)

    display(button, output)

    def on_button_clicked(b):
        
        with open("answers.json", "r") as f:
            source_dict = json.load(f)
            
        answer_dict = {
            "ex8": {
                "hist": hist.value
            }
        }
        
        source_dict.update(answer_dict)
        
        with open("answers.json", "w") as f:
            json.dump(source_dict, f)
            
        with output:
            print("Answer for exercise 8 saved.")
            

    button.on_click(on_button_clicked)
    
    
def exercise_9():
    mean = widgets.ToggleButtons(
        options=['stays the same', 'increases', 'decreases'],
        description='The mean of the sum:',
        disabled=False,
        button_style='',
    )
    
    var = widgets.ToggleButtons(
        options=['stays the same', 'increases', 'decreases'],
        description='The variance of the sum:',
        disabled=False,
        button_style='',
    )
    
    cov = widgets.ToggleButtons(
        options=['stays the same', 'increases', 'decreases'],
        description='The covariance of the joint distribution:',
        disabled=False,
        button_style='',
    )
    
    button = widgets.Button(description="Save your answer!", button_style="success")
    output = widgets.Output()
    
    print("As the number of sides in the die increases:")
    display(mean)
    display(var)
    display(cov)

    display(button, output)

    def on_button_clicked(b):
        
        with open("answers.json", "r") as f:
            source_dict = json.load(f)
            
        answer_dict = {
            "ex9": {
                "mean": mean.value,
                "var": var.value,
                "cov": cov.value,
            }
        }
        
        source_dict.update(answer_dict)
        
        with open("answers.json", "w") as f:
            json.dump(source_dict, f)
            
        with output:
            print("Answer for exercise 9 saved.")
            

    button.on_click(on_button_clicked)
    
    

def exercise_10():
    options = widgets.RadioButtons(
                options=[
                    'the mean and variance is the same regardless of which side is loaded', 
                    'having the sides 3 or 4 loaded will yield a higher covariance than any other sides', 
                    'the mean will decrease as the value of the loaded side increases', 
                    'changing the loaded side from 1 to 6 will yield a higher mean but the same variance'
                ],
                layout={'width': 'max-content'}
            )
    
    button = widgets.Button(description="Save your answer!", button_style="success")
    output = widgets.Output()
    
    display(options)

    display(button, output)

    def on_button_clicked(b):
        
        with open("answers.json", "r") as f:
            source_dict = json.load(f)
            
        answer_dict = {
            "ex10": {
                "options": options.value,
            }
        }
        
        source_dict.update(answer_dict)
        
        with open("answers.json", "w") as f:
            json.dump(source_dict, f)
            
        with output:
            print("Answer for exercise 10 saved.")
            

    button.on_click(on_button_clicked)
    
    
def exercise_11():
    options = widgets.RadioButtons(
                options=[
                    'yes, but only if one of the sides is loaded', 
                    'no, regardless if the die is fair or not', 
                    'yes, but only if the die is fair', 
                    'yes, regardless if the die is fair or not'
                ],
                layout={'width': 'max-content'}
            )
    
    button = widgets.Button(description="Save your answer!", button_style="success")
    output = widgets.Output()
    
    display(options)

    display(button, output)

    def on_button_clicked(b):
        
        with open("answers.json", "r") as f:
            source_dict = json.load(f)
            
        answer_dict = {
            "ex11": {
                "options": options.value,
            }
        }
        
        source_dict.update(answer_dict)
        
        with open("answers.json", "w") as f:
            json.dump(source_dict, f)
            
        with output:
            print("Answer for exercise 11 saved.")
            

    button.on_click(on_button_clicked)
    
    
def check_submissions():
    with open("./answers.json", "r") as f:
        answer_dict = json.load(f)
        
    saved_exercises = [k for k in answer_dict.keys()]
    expected = ['ex1', 'ex2', 'ex3', 'ex4', 'ex5', 'ex6', 'ex7', 'ex8', 'ex9', 'ex10', 'ex11']
    missing = [e for e in expected if not e in saved_exercises]
    
    if missing:
        print(f"missing answers for exercises {[ex.split('ex')[1] for ex in missing]}\n\nSave your answers before submitting for grading!")
        return
    
    print("All answers saved, you can submit the assignment for grading!")


df_anscombe = pd.read_csv('df_anscombe.csv')
df_datasaurus = pd.read_csv("datasaurus.csv")

def plot_anscombes_quartet():
    fig, axs = plt.subplots(2,2, figsize = (8,5), tight_layout = True)
    i = 1
    fig.suptitle("Anscombe's quartet", fontsize = 16)
    for line in axs:
        for ax in line:
            ax.scatter(df_anscombe[df_anscombe.group == i]['x'],df_anscombe[df_anscombe.group == i]['y'])
            ax.set_title(f'Group {i}')
            ax.set_ylim(2,15)
            ax.set_xlim(0,21)
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            i+=1
        
def display_widget():

    dropdown_graph_1 = widgets.Dropdown(
    options=df_datasaurus.group.unique(),
    value='dino',
    description='Data set 1: ',
    disabled=False,
)
    
    statistics_graph_1 = widgets.Button(
    value=False,
    description='Compute stats',
    disabled=False,
    button_style='',
    tooltip='Description',
    icon='' 
)

    dropdown_graph_2 = widgets.Dropdown(
    options=df_datasaurus.group.unique(),
    value='h_lines',
    description='Data set 2: ',
    disabled=False,
)
    
    statistics_graph_2 = widgets.Button(
    value=False,
    description='Compute stats',
    disabled=False,
    button_style='',
    tooltip='Description',
    icon='' 
)
    plotted_stats_graph_1 = None
    plotted_stats_graph_2 = None

    fig = plt.figure(figsize = (8,4), tight_layout = True)
    gs = gridspec.GridSpec(2,2)
    ax_1 = fig.add_subplot(gs[0,0])
    ax_2 = fig.add_subplot(gs[1,0])
    ax_text_1 = fig.add_subplot(gs[0,1])
    ax_text_2 = fig.add_subplot(gs[1,1])
    df_group_1 = df_datasaurus.groupby('group').get_group('dino')
    df_group_2 = df_datasaurus.groupby('group').get_group('h_lines')
    sc_1 = ax_1.scatter(df_group_1['x'],df_group_1['y'], s = 4)
    sc_2 = ax_2.scatter(df_group_2['x'],df_group_2['y'], s = 4)
    ax_1.set_xlabel('x')
    ax_1.set_ylabel('y')
    ax_2.set_xlabel('x')
    ax_2.set_ylabel('y')
    ax_text_1.axis('off')
    ax_text_2.axis('off')
    
    def dropdown_choice(value, plotted_stats, ax_text, sc):
        if value.new != plotted_stats:
            ax_text.clear()
            ax_text.axis('off')
        sc.set_offsets(df_datasaurus.groupby('group').get_group(value.new)[['x', 'y']])
        fig.canvas.draw_idle()
    
        
    def get_stats(value, plotted_stats, ax_text, dropdown, val):
        value = dropdown.value
        if value == plotted_stats:
            return
        ax_text.clear()
        ax_text.axis('off')
        df_group = df_datasaurus.groupby('group').get_group(value)[['x','y']]
        means = df_group.mean()
        var = df_group.var()
        corr = df_group.corr()
        ax_text.text(0,
                    0,
                    f"Statistics:\n      Mean x:      {means['x']:.2f}\n      Variance x: {var['x']:.2f}\n\n      Mean y:      {means['y']:.2f}\n      Variance y: {var['y']:.2f}\n\n      Correlation:  {corr['x']['y']:.2f}"
                    )
        if val == 1:
            plotted_stats_graph_1 = value
        if val == 2:
            plotted_stats_graph_2 = value
        
        
        

    dropdown_graph_1.observe(lambda value: dropdown_choice(value,plotted_stats_graph_1, ax_text_1, sc_1), names = 'value')
    statistics_graph_1.on_click(lambda value: get_stats(value, plotted_stats_graph_1, ax_text_1, dropdown_graph_1,1))
    dropdown_graph_2.observe(lambda value: dropdown_choice(value,plotted_stats_graph_2, ax_text_2, sc_2), names = 'value')
    statistics_graph_2.on_click(lambda value: get_stats(value, plotted_stats_graph_2, ax_text_2, dropdown_graph_2,2))    
    graph_1_box = HBox([dropdown_graph_1, statistics_graph_1])
    graph_2_box = HBox([dropdown_graph_2, statistics_graph_2])
    display(VBox([graph_1_box,graph_2_box]))
    

def plot_datasaurus():

    fig, axs = plt.subplots(6,2, figsize = (7,9), tight_layout = True)
    i = 0
    fig.suptitle("Datasaurus", fontsize = 16)
    for line in axs:
        for ax in line:
            if i > 12:
                ax.axis('off')
            else:
                group = df_datasaurus.group.unique()[i]
                ax.scatter(df_datasaurus[df_datasaurus.group == group]['x'],df_datasaurus[df_datasaurus.group == group]['y'], s = 4)
                ax.set_title(f'Group {group}')
                ax.set_ylim(-5,110)
                ax.set_xlim(10,110)
                ax.set_xlabel('x')
                ax.set_ylabel('y')
                i+=1

