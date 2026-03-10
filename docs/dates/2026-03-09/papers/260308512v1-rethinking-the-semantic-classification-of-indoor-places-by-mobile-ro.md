---
layout: default
title: Rethinking the semantic classification of indoor places by mobile robots
---

# Rethinking the semantic classification of indoor places by mobile robots
**arXiv**：[2603.08512v1](https://arxiv.org/abs/2603.08512) · [PDF](https://arxiv.org/pdf/2603.08512.pdf)  
**作者**：Oscar Martinez Mozos, Alejandra C. Hernandez, Clara Gomez, Ramon Barber  

**一句话要点**：提出允许室内语义分类混淆的新范式，以增强服务机器人适应性。

**关键词**：室内语义分类, 服务机器人, 语义理解, 混淆允许, 物体搜索

## 3 点简述
- 核心问题：传统方法将室内区域按完整房间分类，但同一房间内不同区域可能有不同用途，导致语义理解僵化。
- 方法要点：放松语义分类器的标签输出，允许房间内部出现混淆，以适应动态使用场景。
- 实验或效果：在物体搜索任务中进行了概念验证，未知具体性能提升。

## 摘要（原文）

> A significant challenge in service robots is the semantic understanding of their surrounding areas. Traditional approaches addressed this problem by segmenting the floor plan into regions corresponding to full rooms that are assigned labels consistent with human perception, e.g. office or kitchen. However, different areas inside the same room can be used in different ways: Could the table and the chair in my kitchen become my office? What is the category of that area now? office or kitchen? To adapt to these circumstances we propose a new paradigm where we intentionally relax the resulting labeling of semantic classifiers by allowing confusions inside rooms. Our hypothesis is that those confusions can be beneficial to a service robot. We present a proof of concept in the task of searching for objects.

