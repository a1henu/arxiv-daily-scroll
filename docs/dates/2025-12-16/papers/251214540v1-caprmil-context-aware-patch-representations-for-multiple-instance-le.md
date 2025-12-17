---
layout: default
title: CAPRMIL: Context-Aware Patch Representations for Multiple Instance Learning
---

# CAPRMIL: Context-Aware Patch Representations for Multiple Instance Learning
**arXiv**：[2512.14540v1](https://arxiv.org/abs/2512.14540) · [PDF](https://arxiv.org/pdf/2512.14540.pdf)  
**作者**：Andreas Lolos, Theofilos Christodoulou, Aris L. Moustakas, Stergios Christodoulidis, Maria Vakalopoulou  

**一句话要点**：提出CAPRMIL框架，通过上下文感知补丁表示提升计算病理学中弱监督学习效率

**关键词**：计算病理学, 多实例学习, 弱监督学习, 上下文感知表示, 高效聚合, 自注意力机制

## 3 点简述
- 针对计算病理学中全切片图像标注稀缺，提出基于多实例学习的弱监督方法，简化聚合器设计
- 利用冻结补丁编码器提取特征，通过全局上下文令牌和自注意力注入上下文，降低计算复杂度
- 在多个公开病理基准测试中匹配SOTA性能，大幅减少参数、FLOPs和训练时间，提升可扩展性

## 摘要（原文）

> In computational pathology, weak supervision has become the standard for deep learning due to the gigapixel scale of WSIs and the scarcity of pixel-level annotations, with Multiple Instance Learning (MIL) established as the principal framework for slide-level model training. In this paper, we introduce a novel setting for MIL methods, inspired by proceedings in Neural Partial Differential Equation (PDE) Solvers. Instead of relying on complex attention-based aggregation, we propose an efficient, aggregator-agnostic framework that removes the complexity of correlation learning from the MIL aggregator. CAPRMIL produces rich context-aware patch embeddings that promote effective correlation learning on downstream tasks. By projecting patch features -- extracted using a frozen patch encoder -- into a small set of global context/morphology-aware tokens and utilizing multi-head self-attention, CAPRMIL injects global context with linear computational complexity with respect to the bag size. Paired with a simple Mean MIL aggregator, CAPRMIL matches state-of-the-art slide-level performance across multiple public pathology benchmarks, while reducing the total number of trainable parameters by 48%-92.8% versus SOTA MILs, lowering FLOPs during inference by 52%-99%, and ranking among the best models on GPU memory efficiency and training time. Our results indicate that learning rich, context-aware instance representations before aggregation is an effective and scalable alternative to complex pooling for whole-slide analysis. Our code is available at https://github.com/mandlos/CAPRMIL

