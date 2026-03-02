---
layout: default
title: Multimodal Optimal Transport for Unsupervised Temporal Segmentation in Surgical Robotics
---

# Multimodal Optimal Transport for Unsupervised Temporal Segmentation in Surgical Robotics
**arXiv**：[2602.24138v1](https://arxiv.org/abs/2602.24138) · [PDF](https://arxiv.org/pdf/2602.24138.pdf)  
**作者**：Omar Mohamed, Edoardo Fazzari, Ayah Al-Naji, Hamdan Alhadhrami, Khalfan Hableel, Saif Alkindi, Cesare Stefanini  

**一句话要点**：提出TASOT方法，通过多模态最优传输实现无监督手术视频时序分割，无需大规模预训练。

**关键词**：手术视频分析, 无监督学习, 多模态最优传输, 时序动作分割, 零样本识别

## 3 点简述
- 核心问题：手术视频相位和步骤识别依赖大规模标注数据，计算和收集成本高。
- 方法要点：结合视觉和文本信息，基于不平衡Gromov-Wasserstein公式进行多模态最优传输对齐。
- 实验或效果：在多个手术数据集上显著优于现有零样本方法，提升幅度达4.5至23.7个百分点。

## 摘要（原文）

> Recognizing surgical phases and steps from video is a fundamental problem in computer-assisted interventions. Recent approaches increasingly rely on large-scale pre-training on thousands of labeled surgical videos, followed by zero-shot transfer to specific procedures. While effective, this strategy incurs substantial computational and data collection costs. In this work, we question whether such heavy pre-training is truly necessary. We propose Text-Augmented Action Segmentation Optimal Transport (TASOT), an unsupervised method for surgical phase and step recognition that extends Action Segmentation Optimal Transport (ASOT) by incorporating textual information generated directly from the videos. TASOT formulates temporal action segmentation as a multimodal optimal transport problem, where the matching cost is defined as a weighted combination of visual and text-based costs. The visual term captures frame-level appearance similarity, while the text term provides complementary semantic cues, and both are jointly regularized through a temporally consistent unbalanced Gromov-Wasserstein formulation. This design enables effective alignment between video frames and surgical actions without surgical-specific pretraining or external web-scale supervision. We evaluate TASOT on multiple benchmark surgical datasets and observe consistent and substantial improvements over existing zero-shot methods, including StrasBypass70 (+23.7), BernBypass70 (+4.5), Cholec80 (+16.5), and AutoLaparo (+19.6). These results demonstrate that fine-grained surgical understanding can be achieved by exploiting information already present in standard visual and textual representations, without resorting to increasingly complex pre-training pipelines. The code will be available at https://github.com/omar8ahmed9/TASOT.

