---
layout: default
title: Depth-Copy-Paste: Multimodal and Depth-Aware Compositing for Robust Face Detection
---

# Depth-Copy-Paste: Multimodal and Depth-Aware Compositing for Robust Face Detection
**arXiv**：[2512.11683v1](https://arxiv.org/abs/2512.11683) · [PDF](https://arxiv.org/pdf/2512.11683.pdf)  
**作者**：Qiushi Guo  

**一句话要点**：提出Depth-Copy-Paste以解决传统复制粘贴增强在面部检测中不真实的问题

**关键词**：数据增强, 面部检测, 深度感知, 语义兼容, 复制粘贴

## 3 点简述
- 传统复制粘贴增强因前景提取不准和几何不一致导致不真实合成
- 方法结合BLIP、CLIP、SAM3和Depth-Anything实现语义兼容和深度感知的增强
- 实验显示该方法提升面部检测性能，优于传统方法

## 摘要（原文）

> Data augmentation is crucial for improving the robustness of face detection systems, especially under challenging conditions such as occlusion, illumination variation, and complex environments. Traditional copy paste augmentation often produces unrealistic composites due to inaccurate foreground extraction, inconsistent scene geometry, and mismatched background semantics. To address these limitations, we propose Depth Copy Paste, a multimodal and depth aware augmentation framework that generates diverse and physically consistent face detection training samples by copying full body person instances and pasting them into semantically compatible scenes. Our approach first employs BLIP and CLIP to jointly assess semantic and visual coherence, enabling automatic retrieval of the most suitable background images for the given foreground person. To ensure high quality foreground masks that preserve facial details, we integrate SAM3 for precise segmentation and Depth-Anything to extract only the non occluded visible person regions, preventing corrupted facial textures from being used in augmentation. For geometric realism, we introduce a depth guided sliding window placement mechanism that searches over the background depth map to identify paste locations with optimal depth continuity and scale alignment. The resulting composites exhibit natural depth relationships and improved visual plausibility. Extensive experiments show that Depth Copy Paste provides more diverse and realistic training data, leading to significant performance improvements in downstream face detection tasks compared with traditional copy paste and depth free augmentation methods.

