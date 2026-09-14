from memory_profiler import memory_usage
import random
import time


names = ['Blessing', 'Onoh', ' Julius', 'Oluwaseyi', 'Nasifat', 'Emediong']
majors = ['Physics', 'Math', 'CompSci', 'MechEng.', 'Arts', 'Business']

memory_before = memory_usage()[0]
memory_after = memory_usage()[0]

print(f'Memory (Before): {memory_before:.2f}Mb')

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


# def people_generator(num_people):
#     for i in range(num_people):
#         person = {
#             'id': i,
#             'name': random.choice(names),
#             'major': random.choice(majors)
#         }
#         yield(person)

t1 = time.process_time()
people = people_list(1000_000)
t2 = time.process_time()

# t1 = time.process_time()
# people = people_generator(1000_000)
# t2 = time.process_time()


print(f"Memory (After) : {memory_after:.2f}Mb'")
print(f'Took {t2 - t1} seconds')