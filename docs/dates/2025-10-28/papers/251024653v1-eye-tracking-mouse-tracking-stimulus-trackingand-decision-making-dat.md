---
layout: default
title: Eye-Tracking, Mouse Tracking, Stimulus Tracking,and Decision-Making Datasets in Digital Pathology
---

# Eye-Tracking, Mouse Tracking, Stimulus Tracking,and Decision-Making Datasets in Digital Pathology
**arXiv**：[2510.24653v1](https://arxiv.org/abs/2510.24653) · [PDF](https://arxiv.org/pdf/2510.24653.pdf)  
**作者**：Veronica Thai, Rui Li, Meng Ling, Shuning Jiang, Jeremy Wolfe, Raghu Machiraju, Yan Hu, Zaibo Li, Anil Parwani, Jian Chen  

**一句话要点**：提出PathoGaze1.0数据集以解决病理诊断中视觉搜索和决策过程的行为数据缺失问题。

**关键词**：数字病理学, 眼动追踪, 行为数据集, 视觉搜索, 决策过程, AI训练

## 3 点简述
- 核心问题：病理学家解读全切片图像时诊断准确率约70%，且缺乏行为数据解释错误和不一致性。
- 方法要点：通过PTAH测试平台收集眼动、鼠标交互、刺激跟踪和决策数据，强调生态效度。
- 实验或效果：记录19位病理学家397张图像数据，包括17万+注视和180万+鼠标事件，可用于训练病理学家和AI系统。

## 摘要（原文）

> Interpretation of giga-pixel whole-slide images (WSIs) is an important but
> difficult task for pathologists. Their diagnostic accuracy is estimated to
> average around 70%. Adding a second pathologist does not substantially improve
> decision consistency. The field lacks adequate behavioral data to explain
> diagnostic errors and inconsistencies. To fill in this gap, we present
> PathoGaze1.0, a comprehensive behavioral dataset capturing the dynamic visual
> search and decision-making processes of the full diagnostic workflow during
> cancer diagnosis. The dataset comprises 18.69 hours of eye-tracking, mouse
> interaction, stimulus tracking, viewport navigation, and diagnostic decision
> data (EMSVD) collected from 19 pathologists interpreting 397 WSIs. The data
> collection process emphasizes ecological validity through an
> application-grounded testbed, called PTAH. In total, we recorded 171,909
> fixations, 263,320 saccades, and 1,867,362 mouse interaction events. In
> addition, such data could also be used to improve the training of both
> pathologists and AI systems that might support human experts. All experiments
> were preregistered at https://osf.io/hj9a7, and the complete dataset along with
> analysis code is available at https://go.osu.edu/pathogaze.

