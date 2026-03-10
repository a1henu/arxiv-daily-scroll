---
layout: default
title: EndoSERV: A Vision-based Endoluminal Robot Navigation System
---

# EndoSERV: A Vision-based Endoluminal Robot Navigation System
**arXiv**：[2603.08324v1](https://arxiv.org/abs/2603.08324) · [PDF](https://arxiv.org/pdf/2603.08324.pdf)  
**作者**：Junyang Wu, Fangfang Xie, Minghui Zhang, Hanxiao Zhang, Jiayuan Sun, Yun Gu, Guang-Zhong Yang  

**一句话要点**：提出EndoSERV视觉定位方法以解决内腔机器人导航中的组织变形和特征不足问题。

**关键词**：内腔机器人导航, 视觉定位, 分段里程计, 实到虚映射, 无标签训练

## 3 点简述
- 核心问题：内腔解剖结构复杂狭窄，现有视觉定位易受组织变形和体内伪影影响，缺乏稳定地标。
- 方法要点：采用分段到结构和实到虚映射，分块估计里程计，通过迁移技术利用虚拟姿态真值训练。
- 实验或效果：在公共和临床数据集上验证，无需真实姿态标签即可有效定位。

## 摘要（原文）

> Robot-assisted endoluminal procedures are increasingly used for early cancer intervention. However, the intricate, narrow and tortuous pathways within the luminal anatomy pose substantial difficulties for robot navigation. Vision-based navigation offers a promising solution, but existing localization approaches are error-prone due to tissue deformation, in vivo artifacts and a lack of distinctive landmarks for consistent localization. This paper presents a novel EndoSERV localization method to address these challenges. It includes two main parts, \textit{i.e.}, \textbf{SE}gment-to-structure and \textbf{R}eal-to-\textbf{V}irtual mapping, and hence the name. For long-range and complex luminal structures, we divide them into smaller sub-segments and estimate the odometry independently. To cater for label insufficiency, an efficient transfer technique maps real image features to the virtual domain to use virtual pose ground truth. The training phases of EndoSERV include an offline pretraining to extract texture-agnostic features, and an online phase that adapts to real-world conditions. Extensive experiments based on both public and clinical datasets have been performed to demonstrate the effectiveness of the method even without any real pose labels.

