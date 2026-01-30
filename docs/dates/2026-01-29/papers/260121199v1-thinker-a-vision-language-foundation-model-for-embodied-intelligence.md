---
layout: default
title: Thinker: A vision-language foundation model for embodied intelligence
---

# Thinker: A vision-language foundation model for embodied intelligence
**arXiv**：[2601.21199v1](https://arxiv.org/abs/2601.21199) · [PDF](https://arxiv.org/pdf/2601.21199.pdf)  
**作者**：Baiyu Pan, Daqin Luo, Junpeng Yang, Jiyuan Wang, Yixuan Zhang, Hailin Shi, Jichao Jiao  

**一句话要点**：提出Thinker视觉语言基础模型，通过构建专用数据集和联合关键帧与全视频输入，解决机器人领域视角混淆和时序推理问题。

**关键词**：视觉语言模型, 机器人感知, 视频理解, 时序推理, 数据集构建

## 3 点简述
- 核心问题：大视觉语言模型在机器人应用中易混淆第一与第三人称视角，并忽视视频结尾信息。
- 方法要点：构建大规模机器人感知与推理数据集，并联合关键帧和全视频序列输入以增强视频理解能力。
- 实验或效果：在任务规划领域两个常用基准数据集上取得最先进结果。

## 摘要（原文）

> When large vision-language models are applied to the field of robotics, they encounter problems that are simple for humans yet error-prone for models. Such issues include confusion between third-person and first-person perspectives and a tendency to overlook information in video endings during temporal reasoning. To address these challenges, we propose Thinker, a large vision-language foundation model designed for embodied intelligence. We tackle the aforementioned issues from two perspectives. Firstly, we construct a large-scale dataset tailored for robotic perception and reasoning, encompassing ego-view videos, visual grounding, spatial understanding, and chain-of-thought data. Secondly, we introduce a simple yet effective approach that substantially enhances the model's capacity for video comprehension by jointly incorporating key frames and full video sequences as inputs. Our model achieves state-of-the-art results on two of the most commonly used benchmark datasets in the field of task planning.

