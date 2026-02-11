---
layout: default
title: RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation
---

# RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation
**arXiv**：[2602.09973v1](https://arxiv.org/abs/2602.09973) · [PDF](https://arxiv.org/pdf/2602.09973.pdf)  
**作者**：Hao Li, Ziqin Wang, Zi-han Ding, Shuai Yang, Yilun Chen, Yang Tian, Xiaolin Hu, Tai Wang, Dahua Lin, Feng Zhao, Si Liu, Jiangmiao Pang  

**一句话要点**：提出RoboInter中间表示套件以解决机器人操作中数据稀缺与泛化不足问题

**关键词**：机器人操作, 中间表示, 视觉语言动作模型, 数据集构建, 规划执行框架, 具身推理

## 3 点简述
- 现有机器人操作数据集成本高、泛化差，缺乏中间监督阻碍VLA模型发展
- RoboInter提供大规模数据集与标注工具，支持10类以上中间表示的密集标注
- 引入VQA基准和VLA框架，通过中间表示增强机器人推理与执行能力

## 摘要（原文）

> Advances in large vision-language models (VLMs) have stimulated growing interest in vision-language-action (VLA) systems for robot manipulation. However, existing manipulation datasets remain costly to curate, highly embodiment-specific, and insufficient in coverage and diversity, thereby hindering the generalization of VLA models. Recent approaches attempt to mitigate these limitations via a plan-then-execute paradigm, where high-level plans (e.g., subtasks, trace) are first generated and subsequently translated into low-level actions, but they critically rely on extra intermediate supervision, which is largely absent from existing datasets. To bridge this gap, we introduce the RoboInter Manipulation Suite, a unified resource including data, benchmarks, and models of intermediate representations for manipulation. It comprises RoboInter-Tool, a lightweight GUI that enables semi-automatic annotation of diverse representations, and RoboInter-Data, a large-scale dataset containing over 230k episodes across 571 diverse scenes, which provides dense per-frame annotations over more than 10 categories of intermediate representations, substantially exceeding prior work in scale and annotation quality. Building upon this foundation, RoboInter-VQA introduces 9 spatial and 20 temporal embodied VQA categories to systematically benchmark and enhance the embodied reasoning capabilities of VLMs. Meanwhile, RoboInter-VLA offers an integrated plan-then-execute framework, supporting modular and end-to-end VLA variants that bridge high-level planning with low-level execution via intermediate supervision. In total, RoboInter establishes a practical foundation for advancing robust and generalizable robotic learning via fine-grained and diverse intermediate representations.

