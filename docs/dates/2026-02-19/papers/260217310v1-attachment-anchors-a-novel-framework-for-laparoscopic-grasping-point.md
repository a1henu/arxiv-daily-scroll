---
layout: default
title: Attachment Anchors: A Novel Framework for Laparoscopic Grasping Point Prediction in Colorectal Surgery
---

# Attachment Anchors: A Novel Framework for Laparoscopic Grasping Point Prediction in Colorectal Surgery
**arXiv**：[2602.17310v1](https://arxiv.org/abs/2602.17310) · [PDF](https://arxiv.org/pdf/2602.17310.pdf)  
**作者**：Dennis N. Schneider, Lars Wagner, Daniel Rueckert, Dirk Wilhelm  

**一句话要点**：提出附件锚点框架，用于结直肠手术中腹腔镜抓取点预测，以提升自主组织操作准确性。

**关键词**：腹腔镜手术, 抓取点预测, 结直肠手术, 机器学习, 组织操作, 附件锚点

## 3 点简述
- 核心问题：结直肠手术中自主组织操作的抓取点预测因场景复杂多变而具有挑战性，现有研究不足。
- 方法要点：引入附件锚点作为结构化表示，编码组织与解剖附件的局部几何和力学关系，归一化手术场景以减少不确定性。
- 实验或效果：在90例结直肠手术数据集上验证，附件锚点优于仅基于图像的基线，尤其在分布外设置中表现突出。

## 摘要（原文）

> Accurate grasping point prediction is a key challenge for autonomous tissue manipulation in minimally invasive surgery, particularly in complex and variable procedures such as colorectal interventions. Due to their complexity and prolonged duration, colorectal procedures have been underrepresented in current research. At the same time, they pose a particularly interesting learning environment due to repetitive tissue manipulation, making them a promising entry point for autonomous, machine learning-driven support. Therefore, in this work, we introduce attachment anchors, a structured representation that encodes the local geometric and mechanical relationships between tissue and its anatomical attachments in colorectal surgery. This representation reduces uncertainty in grasping point prediction by normalizing surgical scenes into a consistent local reference frame. We demonstrate that attachment anchors can be predicted from laparoscopic images and incorporated into a grasping framework based on machine learning. Experiments on a dataset of 90 colorectal surgeries demonstrate that attachment anchors improve grasping point prediction compared to image-only baselines. There are particularly strong gains in out-of-distribution settings, including unseen procedures and operating surgeons. These results suggest that attachment anchors are an effective intermediate representation for learning-based tissue manipulation in colorectal surgery.

