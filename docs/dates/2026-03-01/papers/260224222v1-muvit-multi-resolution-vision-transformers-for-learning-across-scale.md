---
layout: default
title: MuViT: Multi-Resolution Vision Transformers for Learning Across Scales in Microscopy
---

# MuViT: Multi-Resolution Vision Transformers for Learning Across Scales in Microscopy
**arXiv**：[2602.24222v1](https://arxiv.org/abs/2602.24222) · [PDF](https://arxiv.org/pdf/2602.24222.pdf)  
**作者**：Albert Dominguez Mantes, Gioele La Manno, Martin Weigert  

**一句话要点**：提出MuViT以融合多分辨率显微镜图像，通过世界坐标建模提升跨尺度分析性能

**关键词**：多分辨率视觉Transformer, 显微镜图像分析, 世界坐标建模, 跨尺度学习, 旋转位置编码, 自监督预训练

## 3 点简述
- 显微镜图像多尺度结构需融合，但现有模型多基于单分辨率或单视图，限制多分辨率信息利用
- MuViT嵌入所有图像块到共享世界坐标系，扩展旋转位置编码，使注意力机制能整合宽场上下文与高分辨率细节
- 在合成基准、肾脏组织病理学和高分辨率小鼠脑显微镜实验中，MuViT优于ViT和CNN基线，多分辨率MAE预训练增强下游任务

## 摘要（原文）

> Modern microscopy routinely produces gigapixel images that contain structures across multiple spatial scales, from fine cellular morphology to broader tissue organization. Many analysis tasks require combining these scales, yet most vision models operate at a single resolution or derive multi-scale features from one view, limiting their ability to exploit the inherently multi-resolution nature of microscopy data. We introduce MuViT, a transformer architecture built to fuse true multi-resolution observations from the same underlying image. MuViT embeds all patches into a shared world-coordinate system and extends rotary positional embeddings to these coordinates, enabling attention to integrate wide-field context with high-resolution detail within a single encoder. Across synthetic benchmarks, kidney histopathology, and high-resolution mouse-brain microscopy, MuViT delivers consistent improvements over strong ViT and CNN baselines. Multi-resolution MAE pretraining further produces scale-consistent representations that enhance downstream tasks. These results demonstrate that explicit world-coordinate modelling provides a simple yet powerful mechanism for leveraging multi-resolution information in large-scale microscopy analysis.

