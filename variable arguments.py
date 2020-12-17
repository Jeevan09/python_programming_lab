print("\nvariable length arguments")
def varlen(name,*fav_food):
    print("name:",name)
    print("your favorite food :")
    for food in fav_food:
        print(food)
varlen("SaiKiran","biryani","rabdi","belgium chocolate","chizza")
