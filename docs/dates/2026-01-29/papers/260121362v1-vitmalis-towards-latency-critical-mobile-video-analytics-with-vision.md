---
layout: default
title: ViTMAlis: Towards Latency-Critical Mobile Video Analytics with Vision Transformers
---

# ViTMAlis: Towards Latency-Critical Mobile Video Analytics with Vision Transformers
**arXiv**：[2601.21362v1](https://arxiv.org/abs/2601.21362) · [PDF](https://arxiv.org/pdf/2601.21362.pdf)  
**作者**：Miao Zhang, Guanzhen Wu, Hao Fang, Yifei Zhu, Fangxin Wang, Ruixiao Zhang, Jiangchuan Liu  

**一句话要点**：提出ViTMAlis框架，通过动态混合分辨率推理和ViT原生卸载，解决移动视频分析中延迟关键场景的传输与推理延迟问题。

**关键词**：移动视频分析, 视觉Transformer, 延迟优化, 动态卸载, 混合分辨率推理, 密集预测

## 3 点简述
- 核心问题：ViT模型在移动视频分析中面临高推理延迟，尤其在密集预测任务中，高分辨率输入加剧其二次计算复杂度。
- 方法要点：设计动态混合分辨率推理策略，并构建ViT原生设备到边缘卸载框架，动态适应网络条件和视频内容。
- 实验或效果：在商用设备上实现原型，相比现有基线，显著降低端到端卸载延迟并提升用户感知渲染精度。

## 摘要（原文）

> Edge-assisted mobile video analytics (MVA) applications are increasingly shifting from using vision models based on convolutional neural networks (CNNs) to those built on vision transformers (ViTs) to leverage their superior global context modeling and generalization capabilities. However, deploying these advanced models in latency-critical MVA scenarios presents significant challenges. Unlike traditional CNN-based offloading paradigms where network transmission is the primary bottleneck, ViT-based systems are constrained by substantial inference delays, particularly for dense prediction tasks where the need for high-resolution inputs exacerbates the inherent quadratic computational complexity of ViTs. To address these challenges, we propose a dynamic mixed-resolution inference strategy tailored for ViT-backboned dense prediction models, enabling flexible runtime trade-offs between speed and accuracy. Building on this, we introduce ViTMAlis, a ViT-native device-to-edge offloading framework that dynamically adapts to network conditions and video content to jointly reduce transmission and inference delays. We implement a fully functional prototype of ViTMAlis on commodity mobile and edge devices. Extensive experiments demonstrate that, compared to state-of-the-art accuracy-centric, content-aware, and latency-adaptive baselines, ViTMAlis significantly reduces end-to-end offloading latency while improving user-perceived rendering accuracy, providing a practical foundation for next-generation mobile intelligence.

