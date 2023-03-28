# from util.http_method import Http_methods
#
#
# base_url = "https://swapi.dev/api/"
# people = "people/4/"
# film_1 = "films/1/"
# film_2 = "films/2/"
# film_3 = "films/3/"
# film_6 = "films/6/"
#
# class Google_maps_api():
#
#     @staticmethod
#     def create_new_place():
#         json_for_create_new_place = {
#             "name": "Darth Vader",
#             "height": "202",
#             "mass": "136",
#             "hair_color": "none",
#             "skin_color": "white",
#             "eye_color": "yellow",
#             "birth_year": "41.9BBY",
#             "gender": "male",
#             "homeworld": "https://swapi.dev/api/planets/1/",
#             "films": [
#                 "https://swapi.dev/api/films/1/",
#                 "https://swapi.dev/api/films/2/",
#                 "https://swapi.dev/api/films/3/",
#                 "https://swapi.dev/api/films/6/"
#             ],
#             "species": [],
#             "vehicles": [],
#             "starships": [
#                 "https://swapi.dev/api/starships/13/"
#             ],
#             "created": "2014-12-10T15:18:20.704000Z",
#             "edited": "2014-12-20T21:17:50.313000Z",
#             "url": "https://swapi.dev/api/people/4/"
#         }
#
#         #post_resource = "/maps/api/place/add/json"
#         post_url = base_url + people
#         print(post_url)
#         result_post = Http_methods.post(post_url, json_for_create_new_place)
#         print(result_post.text)
#         return result_post
#
#
#     # @staticmethod
#     # def get_new_place(place_id):
#     #     #get_resiurce = "/maps/api/place/get/json"
#     #     get_url = base_url + people
#     #     print(get_url)
#     #     result_get = Http_methods.get(get_url)
#     #     print(result_get.text)
#     #     return result_get
# #Метод для изменения локации
#     # @staticmethod
#     # def put_new_place(place_id):
#     #     put_resiurce = "/maps/api/place/update/json" #Ресурс метода put
#     #     put_url = base_url + put_resiurce + key
#     #     print(put_url)
#     #     json_for_update_new_location = {
#     #         "place_id": place_id,
#     #
#     #         "address": "100 Lenina street, RU",
#     #
#     #         "key": "qaclick123"
#     #
#     #     }
#     #     result_put = Http_methods.put(put_url,json_for_update_new_location)
#     #     print(result_put.text)
#     #     return result_put
#     #
#     #     # Метод для удаления новой локации
#     # @staticmethod
#     # def delete_new_place(place_id):
#     #         delete_resiurce = "/maps/api/place/delete/json"  # Ресурс метода delete
#     #         put_url = base_url + delete_resiurce + key
#     #         print(put_url)
#     #         json_for_delete_new_location = {
#     #             "place_id": place_id
#     #         }
#     #         result_delete = Http_methods.delete(put_url, json_for_delete_new_location)
#     #         print(result_delete.text)
#     #         return result_delete