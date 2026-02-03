---
layout: default
title: Back to the Future: Look-ahead Augmentation and Parallel Self-Refinement for Time Series Forecasting
---

# Back to the Future: Look-ahead Augmentation and Parallel Self-Refinement for Time Series Forecasting
**arXiv**：[2602.02146v1](https://arxiv.org/abs/2602.02146) · [PDF](https://arxiv.org/pdf/2602.02146.pdf)  
**作者**：Sunho Kim, Susik Yoon  

**一句话要点**：提出BTTF框架，通过前瞻增强与并行自精炼提升长期时间序列预测的稳定性与准确性。

**关键词**：时间序列预测, 长期预测, 模型增强, 自精炼, 并行预测, 稳定性提升

## 3 点简述
- 核心问题：长期时间序列预测中，直接多步预测与迭代多步预测在并行效率与时间一致性间存在权衡。
- 方法要点：基于基础模型预测进行前瞻增强，通过第二阶段模型集成实现自校正精炼，无需复杂架构。
- 实验或效果：在长期预测中提升准确性达58%，即使在次优训练条件下也能稳定改进，增强线性模型稳定性。

## 摘要（原文）

> Long-term time series forecasting (LTSF) remains challenging due to the trade-off between parallel efficiency and sequential modeling of temporal coherence. Direct multi-step forecasting (DMS) methods enable fast, parallel prediction of all future horizons but often lose temporal consistency across steps, while iterative multi-step forecasting (IMS) preserves temporal dependencies at the cost of error accumulation and slow inference. To bridge this gap, we propose Back to the Future (BTTF), a simple yet effective framework that enhances forecasting stability through look-ahead augmentation and self-corrective refinement. Rather than relying on complex model architectures, BTTF revisits the fundamental forecasting process and refines a base model by ensembling the second-stage models augmented with their initial predictions. Despite its simplicity, our approach consistently improves long-horizon accuracy and mitigates the instability of linear forecasting models, achieving accuracy gains of up to 58% and demonstrating stable improvements even when the first-stage model is trained under suboptimal conditions. These results suggest that leveraging model-generated forecasts as augmentation can be a simple yet powerful way to enhance long-term prediction, even without complex architectures.

