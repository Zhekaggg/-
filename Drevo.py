from pyvis.network import Network

net = Network(notebook=True, cdn_resources="remote")
net.add_nodes([1,2,3,4,5], #есди будешь добовлять имена то добавь тут еще одну цифру
#можешь сама написать имена заместо этих и можешь добавть 
# имена добовляются ,"имя"
        label=["имя", "имя", "имя", "имя","имя"],
#есди будешь добовлять имена то 
        color=["#код цвета", "#код цвета", "#код цвета","#код цвета","#код цвета"]) 
#код цвето можешь кайти в гугле и обезптельно с хештегом

net.add_edges([(1, 2), (2, 3), (3, 4), (4, 1), (1,5)])


net.show("templates/index.html")