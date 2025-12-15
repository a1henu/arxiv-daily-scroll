---
layout: default
title: SSA3D: Text-Conditioned Assisted Self-Supervised Framework for Automatic Dental Abutment Design
---

# SSA3D: Text-Conditioned Assisted Self-Supervised Framework for Automatic Dental Abutment Design
**arXiv**：[2512.11507v1](https://arxiv.org/abs/2512.11507) · [PDF](https://arxiv.org/pdf/2512.11507.pdf)  
**作者**：Mianjie Zheng, Xinquan Yang, Along He, Xuguang Li, Feilie Zhong, Xuefen Liu, Kun Tang, Zhicheng Zhang, Linlin Shen  

**一句话要点**：提出SSA3D框架，通过双分支架构和文本条件提示，实现高效自动牙科基台设计。

**关键词**：牙科基台设计, 自监督学习, 双分支架构, 文本条件提示, 自动参数预测

## 3 点简述
- 核心问题：牙科基台设计依赖人工，AI自动化因标注数据稀缺和自监督学习计算成本高而受限。
- 方法要点：采用重建与回归双分支架构，结合文本条件提示模块，整合临床信息以指导网络预测。
- 实验或效果：在收集数据集上，SSA3D节省一半训练时间，精度优于传统自监督方法，达到先进水平。

## 摘要（原文）

> Abutment design is a critical step in dental implant restoration. However, manual design involves tedious measurement and fitting, and research on automating this process with AI is limited, due to the unavailability of large annotated datasets. Although self-supervised learning (SSL) can alleviate data scarcity, its need for pre-training and fine-tuning results in high computational costs and long training times. In this paper, we propose a Self-supervised assisted automatic abutment design framework (SS$A^3$D), which employs a dual-branch architecture with a reconstruction branch and a regression branch. The reconstruction branch learns to restore masked intraoral scan data and transfers the learned structural information to the regression branch. The regression branch then predicts the abutment parameters under supervised learning, which eliminates the separate pre-training and fine-tuning process. We also design a Text-Conditioned Prompt (TCP) module to incorporate clinical information (such as implant location, system, and series) into SS$A^3$D. This guides the network to focus on relevant regions and constrains the parameter predictions. Extensive experiments on a collected dataset show that SS$A^3$D saves half of the training time and achieves higher accuracy than traditional SSL methods. It also achieves state-of-the-art performance compared to other methods, significantly improving the accuracy and efficiency of automated abutment design.

