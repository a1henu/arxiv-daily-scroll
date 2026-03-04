---
layout: default
title: BRIGHT: A Collaborative Generalist-Specialist Foundation Model for Breast Pathology
---

# BRIGHT: A Collaborative Generalist-Specialist Foundation Model for Breast Pathology
**arXiv**：[2603.03030v1](https://arxiv.org/abs/2603.03030) · [PDF](https://arxiv.org/pdf/2603.03030.pdf)  
**作者**：Xiaojing Guo, Jiatai Lin, Yumian Jia, Jingqi Huang, Zeyan Xu, Weidong Li, Longfei Wang, Jingjing Chen, Qin Li, Weiwei Wang, Lifang Cui, Wen Yue, Zhiqiang Cheng, Xiaolong Wei, Jianzhong Yu, Xia Jin, Baizhou Li, Honghong Shen, Jing Li, Chunlan Li, Yanfen Cui, Yi Dai, Yiling Yang, Xiaolong Qian, Liu Yang, Yang Yang, Guangshen Gao, Yaqing Li, Lili Zhai, Chenying Liu, Tianhua Zhang, Zhenwei Shi, Cheng Lu, Xingchen Zhou, Jing Xu, Miaoqing Zhao, Fang Mei, Jiaojiao Zhou, Ning Mao, Fangfang Liu, Chu Han, Zaiyi Liu  

**一句话要点**：提出BRIGHT以解决乳腺病理学中通用基础模型在器官特异性任务上的不足。

**关键词**：病理基础模型, 乳腺病理学, 协作训练框架, 多任务验证, 全切片图像分析

## 3 点简述
- 核心问题：通用病理基础模型在单一器官系统（如乳腺）的全面临床任务中表现未知，缺乏大规模验证和针对性训练。
- 方法要点：采用协作通用-专家框架，基于约2.1亿病理切片训练，结合通用与器官特异性特征。
- 实验或效果：在24项内部任务中21项达到SOTA，外部验证中5项领先，展示优异临床实用性和可解释性。

## 摘要（原文）

> Generalist pathology foundation models (PFMs), pretrained on large-scale multi-organ datasets, have demonstrated remarkable predictive capabilities across diverse clinical applications. However, their proficiency on the full spectrum of clinically essential tasks within a specific organ system remains an open question due to the lack of large-scale validation cohorts for a single organ as well as the absence of a tailored training paradigm that can effectively translate broad histomorphological knowledge into the organ-specific expertise required for specialist-level interpretation. In this study, we propose BRIGHT, the first PFM specifically designed for breast pathology, trained on approximately 210 million histopathology tiles from over 51,000 breast whole-slide images derived from a cohort of over 40,000 patients across 19 hospitals. BRIGHT employs a collaborative generalist-specialist framework to capture both universal and organ-specific features. To comprehensively evaluate the performance of PFMs on breast oncology, we curate the largest multi-institutional cohorts to date for downstream task development and evaluation, comprising over 25,000 WSIs across 10 hospitals. The validation cohorts cover the full spectrum of breast pathology across 24 distinct clinical tasks spanning diagnosis, biomarker prediction, treatment response and survival prediction. Extensive experiments demonstrate that BRIGHT outperforms three leading generalist PFMs, achieving state-of-the-art (SOTA) performance in 21 of 24 internal validation tasks and in 5 of 10 external validation tasks with excellent heatmap interpretability. By evaluating on large-scale validation cohorts, this study not only demonstrates BRIGHT's clinical utility in breast oncology but also validates a collaborative generalist-specialist paradigm, providing a scalable template for developing PFMs on a specific organ system.

