import xmind
from xmind.core.topic import TopicElement

class MindMap:
    def __init__(self, title, data):
        self.workbook = xmind.load("new.xmind")
        self.sheet = self.workbook.getPrimarySheet()
        self.root_topic = self.sheet.getRootTopic()
        self.root_topic.setTitle(title)
        self.data = data

    def add_subtopics(self):
        for key, values in self.data.items():
            sub_topic = self.root_topic.addSubTopic()
            sub_topic.setTitle(key)
            for value in values:
                sub_sub_topic = sub_topic.addSubTopic()
                sub_sub_topic.setTitle(value)

    def save(self, filename):
        xmind.save(self.workbook, filename)

data = {
    "基础知识准备": ["线性代数", "概率论与统计学", "编程技能"],
    "学习资源选择": ["书籍", "在线课程", "教学视频", "博客和论坛"],
    "学习方法": ["理论学习", "实践项目", "阅读论文", "参与社区"],
    "实践工具": ["TensorFlow", "PyTorch", "Keras", "Jupyter Notebook"]
}

mind_map = MindMap("学习深度学习", data)
mind_map.add_subtopics()
mind_map.save("new.xmind")

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('new.xmind')  # replace with your file path
driver.save_screenshot('screenshot.png')
driver.quit()
