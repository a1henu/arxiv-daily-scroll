---
layout: default
title: Le-DETR: Revisiting Real-Time Detection Transformer with Efficient Encoder Design
---

# Le-DETR: Revisiting Real-Time Detection Transformer with Efficient Encoder Design
**arXiv**：[2602.21010v1](https://arxiv.org/abs/2602.21010) · [PDF](https://arxiv.org/pdf/2602.21010.pdf)  
**作者**：Jiannan Huang, Aditya Kane, Fengzhe Zhou, Yunchao Wei, Humphrey Shi  

**一句话要点**：提出Le-DETR以降低实时检测Transformer的预训练成本并提升性能

**关键词**：实时目标检测, 检测Transformer, 高效骨干网络, 局部注意力, 低预训练成本, 混合编码器设计

## 3 点简述
- 核心问题：现有实时DETR模型因骨干网络预训练开销大，难以复现，限制了新架构探索。
- 方法要点：设计EfficientNAT骨干网络，结合高效卷积与局部注意力，并重构混合编码器以优化速度与性能。
- 实验或效果：在COCO数据集上实现SOTA性能，预训练图像节省约80%，推理速度快且精度高。

## 摘要（原文）

> Real-time object detection is crucial for real-world applications as it requires high accuracy with low latency. While Detection Transformers (DETR) have demonstrated significant performance improvements, current real-time DETR models are challenging to reproduce from scratch due to excessive pre-training overheads on the backbone, constraining research advancements by hindering the exploration of novel backbone architectures. In this paper, we want to show that by using general good design, it is possible to have \textbf{high performance} with \textbf{low pre-training cost}. After a thorough study of the backbone architecture, we propose EfficientNAT at various scales, which incorporates modern efficient convolution and local attention mechanisms. Moreover, we re-design the hybrid encoder with local attention, significantly enhancing both performance and inference speed. Based on these advancements, we present Le-DETR (\textbf{L}ow-cost and \textbf{E}fficient \textbf{DE}tection \textbf{TR}ansformer), which achieves a new \textbf{SOTA} in real-time detection using only ImageNet1K and COCO2017 training datasets, saving about 80\% images in pre-training stage compared with previous methods. We demonstrate that with well-designed, real-time DETR models can achieve strong performance without the need for complex and computationally expensive pretraining. Extensive experiments show that Le-DETR-M/L/X achieves \textbf{52.9/54.3/55.1 mAP} on COCO Val2017 with \textbf{4.45/5.01/6.68 ms} on an RTX4090. It surpasses YOLOv12-L/X by \textbf{+0.6/-0.1 mAP} while achieving similar speed and \textbf{+20\%} speedup. Compared with DEIM-D-FINE, Le-DETR-M achieves \textbf{+0.2 mAP} with slightly faster inference, and surpasses DEIM-D-FINE-L by \textbf{+0.4 mAP} with only \textbf{0.4 ms} additional latency. Code and weights will be open-sourced.

