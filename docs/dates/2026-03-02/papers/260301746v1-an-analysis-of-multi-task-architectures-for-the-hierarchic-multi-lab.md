---
layout: default
title: An Analysis of Multi-Task Architectures for the Hierarchic Multi-Label Problem of Vehicle Model and Make Classification
---

# An Analysis of Multi-Task Architectures for the Hierarchic Multi-Label Problem of Vehicle Model and Make Classification
**arXiv**：[2603.01746v1](https://arxiv.org/abs/2603.01746) · [PDF](https://arxiv.org/pdf/2603.01746.pdf)  
**作者**：Alexandru Manole, Laura Diosan  

**一句话要点**：分析多任务架构在车辆品牌与型号层次多标签分类中的优势与局限

**关键词**：层次多标签分类, 多任务学习, 车辆识别, 卷积神经网络, Transformer, 基准测试

## 3 点简述
- 核心问题：深度学习常忽略信息层次结构，影响车辆品牌与型号分类性能
- 方法要点：比较并行与级联多任务架构，结合CNN和Transformer，调整关键参数
- 实验或效果：在StanfordCars和CompCars数据集上验证多任务学习提升模型性能

## 摘要（原文）

> Most information in our world is organized hierarchically; however, many Deep Learning approaches do not leverage this semantically rich structure. Research suggests that human learning benefits from exploiting the hierarchical structure of information, and intelligent models could similarly take advantage of this through multi-task learning. In this work, we analyze the advantages and limitations of multi-task learning in a hierarchical multi-label classification problem: car make and model classification. Considering both parallel and cascaded multi-task architectures, we evaluate their impact on different Deep Learning classifiers (CNNs, Transformers) while varying key factors such as dropout rate and loss weighting to gain deeper insight into the effectiveness of this approach. The tests are conducted on two established benchmarks: StanfordCars and CompCars. We observe the effectiveness of the multi-task paradigm on both datasets, improving the performance of the investigated CNN in almost all scenarios. Furthermore, the approach yields significant improvements on the CompCars dataset for both types of models.

