# remove matching from the list
my_lis = [["amit", 32], ['srk', 30], ['snl', 28]]
to_del = ['amit', 'srk']

after_del = [i for i in my_lis if i[0] not in to_del]
print(after_del)





#         delete_matching_from_list(sms_cms_attributes)
#
#
# def delete_matching_from_list(sms_cms_attributes):
#     print("len before deleting", len(sms_cms_attributes))
#     start_time = time.time()
#     after_del = [i for i in sms_cms_attributes if i[0] not in attribute_list]
#     print("---------Duration-------- : ", time.time() - start_time)
#     # duration = time.time() - start_time
#     print(len(after_del))
