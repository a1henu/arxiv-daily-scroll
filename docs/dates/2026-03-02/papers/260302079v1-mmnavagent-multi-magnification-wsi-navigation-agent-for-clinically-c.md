---
layout: default
title: MMNavAgent: Multi-Magnification WSI Navigation Agent for Clinically Consistent Whole-Slide Analysis
---

# MMNavAgent: Multi-Magnification WSI Navigation Agent for Clinically Consistent Whole-Slide Analysis
**arXiv**：[2603.02079v1](https://arxiv.org/abs/2603.02079) · [PDF](https://arxiv.org/pdf/2603.02079.pdf)  
**作者**：Zhengyang Xu, Han Li, Jingsong Liu, Linrui Xie, Xun Ma, Xin You, Shihui Zu, Ayako Ito, Xinyu Hao, Hongming Xu, Shaohua Kevin Zhou, Nassir Navab, Peter J. Schüffler  

**一句话要点**：提出多倍率WSI导航代理以解决临床诊断中跨倍率交互与自适应倍率选择问题

**关键词**：全切片图像分析, 多倍率导航, 自适应倍率选择, 临床诊断一致性, 代理框架

## 3 点简述
- 现有WSI诊断方法多基于固定倍率或预定义倍率遍历，与临床多倍率动态检查流程不匹配
- 引入跨倍率导航工具和倍率选择工具，模拟病理学家多倍率交互与自适应选择过程
- 在公开数据集上实验显示诊断性能提升，AUC和BACC分别提高1.45%和2.93%

## 摘要（原文）

> Recent AI navigation approaches aim to improve Whole-Slide Image (WSI) diagnosis by modeling spatial exploration and selecting diagnostically relevant regions, yet most operate at a single fixed magnification or rely on predefined magnification traversal. In clinical practice, pathologists examine slides across multiple magnifications and selectively inspect only necessary scales, dynamically integrating global and cellular evidence in a sequential manner. This mismatch prevents existing methods from modeling cross-magnification interactions and adaptive magnification selection inherent to real diagnostic workflows. To these, we propose a clinically consistent Multi-Magnification WSI Navigation Agent (MMNavAgent) that explicitly models multi magnification interaction and adaptive magnification selection. Specifically, we introduce a Cross-Magnification navigation Tool (CMT) that aggregates contextual information from adjacent magnifications to enhance discriminative representations along the navigation path. We further introduce a Magnification Selection Tool (MST) that leverages memory-driven reasoning within the agent framework to enable interactive and adaptive magnification selection, mimicking the sequential decision process of pathologists. Extensive experiments on a public dataset demonstrate improved diagnostic performance, with 1.45% gain of AUC and 2.93% gain of BACC over a non-agent baseline. Code will be public upon acceptance.

