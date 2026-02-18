---
layout: default
title: ToaSt: Token Channel Selection and Structured Pruning for Efficient ViT
---

# ToaSt: Token Channel Selection and Structured Pruning for Efficient ViT
**arXiv**：[2602.15720v1](https://arxiv.org/abs/2602.15720) · [PDF](https://arxiv.org/pdf/2602.15720.pdf)  
**作者**：Hyunchan Moon, Cheonjun Park, Steven L. Waslander  

**一句话要点**：提出ToaSt框架，通过解耦策略优化ViT计算效率，解决部署中的高计算成本问题。

**关键词**：视觉Transformer, 结构化剪枝, 令牌压缩, 计算效率优化, 模型部署

## 3 点简述
- 核心问题：ViT部署受高计算成本限制，现有结构化剪枝和令牌压缩方法存在重训练时间长和全局传播优化挑战。
- 方法要点：采用解耦框架，对多头自注意力模块应用耦合头结构化剪枝，对前馈网络引入令牌通道选择以提升压缩比。
- 实验或效果：在九个模型上评估，ToaSt在精度和效率间实现优越权衡，如ViT-MAE-Huge上精度提升1.64%且FLOPs减少39.4%。

## 摘要（原文）

> Vision Transformers (ViTs) have achieved remarkable success across various vision tasks, yet their deployment is often hindered by prohibitive computational costs. While structured weight pruning and token compression have emerged as promising solutions, they suffer from prolonged retraining times and global propagation that creates optimization challenges, respectively. We propose ToaSt, a decoupled framework applying specialized strategies to distinct ViT components. We apply coupled head-wise structured pruning to Multi-Head Self-Attention modules, leveraging attention operation characteristics to enhance robustness. For Feed-Forward Networks (over 60\% of FLOPs), we introduce Token Channel Selection (TCS) that enhances compression ratios while avoiding global propagation issues. Our analysis reveals TCS effectively filters redundant noise during selection. Extensive evaluations across nine diverse models, including DeiT, ViT-MAE, and Swin Transformer, demonstrate that ToaSt achieves superior trade-offs between accuracy and efficiency, consistently outperforming existing baselines. On ViT-MAE-Huge, ToaSt achieves 88.52\% accuracy (+1.64 \%) with 39.4\% FLOPs reduction. ToaSt transfers effectively to downstream tasks, cccccachieving 52.2 versus 51.9 mAP on COCO object detection. Code and models will be released upon acceptance.

