import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import graphviz

class MindMap:
    def __init__(self, data):
        self.data = data

        self.G = nx.Graph()  # 创建一个空的无向图对象
        self.pos = None  # 存储节点位置信息的变量
        self.font_path = 'C:\\Windows\Fonts\\simfang.ttf'  # 设置字体路径
        self.font_prop = fm.FontProperties(fname=self.font_path)  # 创建字体属性对象

    def create_hierarchy(self):
        for concept, connections in self.data.items():
            self.G.add_node(concept)  # 添加节点
            for connection in connections:
                self.G.add_edge(concept, connection)  # 添加边

    def visualize(self):
        self.pos = nx.spring_layout(self.G)  # 使用Spring布局算法计算节点位置
        nx.draw(self.G, self.pos, with_labels=True, node_size=5000, node_color='lightblue', font_size=12, font_weight='bold', font_family=self.font_prop.get_name(),node_shape='o')  # 绘制图形
        plt.savefig('mind_map.jpg', dpi=300, bbox_inches='tight')  # 保存图形为jpg格式，并最大化保存
        plt.show()  # 显示图形

data = {
    "学习深度学习": ["基础知识准备", "学习资源选择", "学习方法", "实践工具"],
    "基础知识准备": ["线性代数", "概率论与统计学", "编程技能"],
    "学习资源选择": ["书籍", "在线课程", "教学视频", "博客和论坛"],
    "学习方法": ["理论学习", "实践项目", "阅读论文", "参与社区"],
    "实践工具": ["TensorFlow", "PyTorch", "Keras", "Jupyter Notebook"]
}

mind_map = MindMap(data)  # 创建MindMap对象
mind_map.create_hierarchy()  # 创建图的层次结构
mind_map.visualize()  # 可视化图形

