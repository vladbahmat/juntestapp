from django.shortcuts import render
from .models import Sort
from django.http import HttpResponse
import time


def homepage(request):
    return render(request=request,
                  template_name="operations/home.html",
                  context={"sorts":Sort})


def getData(request):
    return render(request=request,
                  template_name="operations/getData.html",
                  context={"name":Sort.name})
 

def showResult(request):
    filename=request.GET['filetosort']
    select=request.GET['sort_type']
    return render(request=request,
                  template_name='operations/showResult.html',
                  context={
                            'ints':str(add_to_list(filename)),
                            'sorted':str(sortchoice(select,filename))})


def time_of_function(function):
    def wrapped(*args):
        start_time = time.clock()
        res = function(*args)
        print("Time of func: ",time.clock() - start_time)
        return res
    return wrapped


def sortchoice(select,filename):
    if select=="s1":
        return merge_sort(add_to_list(filename))
    elif select=="s2":
        return buble(add_to_list(filename))
    else:
        return insertion_sort(add_to_list(filename))


def add_to_list(filename):
    int_list=[]
    with open(filename) as f:
        for string in f:
            int_list.append([int(x) for x in string.split()])
    return int_list


@time_of_function
def buble(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    return nums


@time_of_function
def insertion_sort(nums):  
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert
    return nums


@time_of_function
def merge_sort(nums):  
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    return merge(left_list, right_list)


def merge(left_list, right_list):  
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)
    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list

