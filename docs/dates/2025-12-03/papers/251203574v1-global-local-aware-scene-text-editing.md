---
layout: default
title: Global-Local Aware Scene Text Editing
---

# Global-Local Aware Scene Text Editing
**arXiv**：[2512.03574v1](https://arxiv.org/abs/2512.03574) · [PDF](https://arxiv.org/pdf/2512.03574.pdf)  
**作者**：Fuxiang Yang, Tonghua Su, Donglin Di, Yin Chen, Xiangqian Wu, Zhongjie Wang, Lei Fan  

**一句话要点**：提出GLASTE框架以解决场景文本编辑中的不一致性和长度不敏感问题

**关键词**：场景文本编辑, 全局-局部感知, 文本风格向量化, 一致性保持, 长度敏感处理

## 3 点简述
- 核心问题：现有方法在编辑后局部与全局不一致，且难以处理文本长度变化
- 方法要点：设计全局-局部组合结构、联合损失和文本风格向量化，确保风格一致与和谐
- 实验或效果：在真实数据集上验证，GLASTE在定量和定性结果上优于先前方法

## 摘要（原文）

> Scene Text Editing (STE) involves replacing text in a scene image with new target text while preserving both the original text style and background texture. Existing methods suffer from two major challenges: inconsistency and length-insensitivity. They often fail to maintain coherence between the edited local patch and the surrounding area, and they struggle to handle significant differences in text length before and after editing. To tackle these challenges, we propose an end-to-end framework called Global-Local Aware Scene Text Editing (GLASTE), which simultaneously incorporates high-level global contextual information along with delicate local features. Specifically, we design a global-local combination structure, joint global and local losses, and enhance text image features to ensure consistency in text style within local patches while maintaining harmony between local and global areas. Additionally, we express the text style as a vector independent of the image size, which can be transferred to target text images of various sizes. We use an affine fusion to fill target text images into the editing patch while maintaining their aspect ratio unchanged. Extensive experiments on real-world datasets validate that our GLASTE model outperforms previous methods in both quantitative metrics and qualitative results and effectively mitigates the two challenges.

