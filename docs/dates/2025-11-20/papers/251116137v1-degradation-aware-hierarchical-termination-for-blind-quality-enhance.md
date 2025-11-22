---
layout: default
title: Degradation-Aware Hierarchical Termination for Blind Quality Enhancement of Compressed Video
---

# Degradation-Aware Hierarchical Termination for Blind Quality Enhancement of Compressed Video
**arXiv**：[2511.16137v1](https://arxiv.org/abs/2511.16137) · [PDF](https://arxiv.org/pdf/2511.16137.pdf)  
**作者**：Li Yu, Yingbo Zhao, Shiyu Wu, Siyue Yu, Moncef Gabbouj, Qingshan Liu  

**一句话要点**：提出退化感知分层终止机制以解决压缩视频盲质量增强中退化信息不足和计算效率低的问题

**关键词**：压缩视频质量增强, 盲方法, 退化表示学习, 分层终止机制, 计算效率优化

## 3 点简述
- 核心问题：现有盲方法依赖全局退化向量，缺乏空间细节，且忽略不同QP的计算需求差异。
- 方法要点：引入预训练退化表示学习模块提取多尺度退化表示，并设计分层终止机制动态调整处理阶段。
- 实验效果：在QP=22时PSNR提升110%，推理时间在QP=22比QP=42减少一半。

## 摘要（原文）

> Existing studies on Quality Enhancement for Compressed Video (QECV) predominantly rely on known Quantization Parameters (QPs), employing distinct enhancement models per QP setting, termed non-blind methods. However, in real-world scenarios involving transcoding or transmission, QPs may be partially or entirely unknown, limiting the applicability of such approaches and motivating the development of blind QECV techniques. Current blind methods generate degradation vectors via classification models with cross-entropy loss, using them as channel attention to guide artifact removal. However, these vectors capture only global degradation information and lack spatial details, hindering adaptation to varying artifact patterns at different spatial positions. To address these limitations, we propose a pretrained Degradation Representation Learning (DRL) module that decouples and extracts high-dimensional, multiscale degradation representations from video content to guide the artifact removal. Additionally, both blind and non-blind methods typically employ uniform architectures across QPs, hence, overlooking the varying computational demands inherent to different compression levels. We thus introduce a hierarchical termination mechanism that dynamically adjusts the number of artifact reduction stages based on the compression level. Experimental results demonstrate that the proposed approach significantly enhances performance, achieving a PSNR improvement of 110% (from 0.31 dB to 0.65 dB) over a competing state-of-the-art blind method at QP = 22. Furthermore, the proposed hierarchical termination mechanism reduces the average inference time at QP = 22 by half compared to QP = 42.

