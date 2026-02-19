---
layout: default
title: Uncertainty-Guided Inference-Time Depth Adaptation for Transformer-Based Visual Tracking
---

# Uncertainty-Guided Inference-Time Depth Adaptation for Transformer-Based Visual Tracking
**arXiv**：[2602.16160v1](https://arxiv.org/abs/2602.16160) · [PDF](https://arxiv.org/pdf/2602.16160.pdf)  
**作者**：Patrick Poggi, Divake Kumar, Theja Tulabandhula, Amit Ranjan Trivedi  

**一句话要点**：提出UncL-STARK方法，通过不确定性引导的推理时深度自适应，降低Transformer跟踪器在长视频中的计算成本。

**关键词**：Transformer跟踪, 深度自适应, 不确定性估计, 知识蒸馏, 计算效率, 长视频跟踪

## 3 点简述
- Transformer跟踪器固定深度推理导致长视频中计算冗余，尤其在时序连贯帧中。
- 采用随机深度训练和知识蒸馏，使模型在多个中间深度保持预测鲁棒性，支持安全截断。
- 运行时基于热图不确定性估计和反馈策略动态选择深度，实验显示显著降低计算、延迟和能耗，精度损失微小。

## 摘要（原文）

> Transformer-based single-object trackers achieve state-of-the-art accuracy but rely on fixed-depth inference, executing the full encoder--decoder stack for every frame regardless of visual complexity, thereby incurring unnecessary computational cost in long video sequences dominated by temporally coherent frames. We propose UncL-STARK, an architecture-preserving approach that enables dynamic, uncertainty-aware depth adaptation in transformer-based trackers without modifying the underlying network or adding auxiliary heads. The model is fine-tuned to retain predictive robustness at multiple intermediate depths using random-depth training with knowledge distillation, thus enabling safe inference-time truncation. At runtime, we derive a lightweight uncertainty estimate directly from the model's corner localization heatmaps and use it in a feedback-driven policy that selects the encoder and decoder depth for the next frame based on the prediction confidence by exploiting temporal coherence in video. Extensive experiments on GOT-10k and LaSOT demonstrate up to 12\% GFLOPs reduction, 8.9\% latency reduction, and 10.8\% energy savings while maintaining tracking accuracy within 0.2\% of the full-depth baseline across both short-term and long-term sequences.

