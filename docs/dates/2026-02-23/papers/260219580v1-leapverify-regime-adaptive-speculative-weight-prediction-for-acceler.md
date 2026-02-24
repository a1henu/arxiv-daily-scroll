---
layout: default
title: Leap+Verify: Regime-Adaptive Speculative Weight Prediction for Accelerating Neural Network Training
---

# Leap+Verify: Regime-Adaptive Speculative Weight Prediction for Accelerating Neural Network Training
**arXiv**：[2602.19580v1](https://arxiv.org/abs/2602.19580) · [PDF](https://arxiv.org/pdf/2602.19580.pdf)  
**作者**：Jeremy McEntire  

**一句话要点**：提出Leap+Verify框架，通过推测性权重预测与验证加速神经网络训练

**关键词**：推测性执行, 训练加速, 权重预测, 阶段检测, 有限差分预测, 损失验证

## 3 点简述
- 核心问题：神经网络训练速度慢，传统优化器状态外推（如动量）在推测性执行中易导致损失爆炸
- 方法要点：基于激活空间余弦相似度动态检测训练阶段（混沌、过渡、稳定），使用有限差分预测器（线性、二次）预测未来权重并验证
- 实验或效果：在GPT-2 124M和Qwen 1.5B上评估，有限差分预测器在稳定或过渡阶段实现24%-37%严格接受率，但大模型可预测阶段更少

## 摘要（原文）

> We introduce Leap+Verify, a framework that applies speculative execution -- predicting future model weights and validating predictions before acceptance -- to accelerate neural network training. Inspired by speculative decoding in language model inference and by the Automatically Scalable Computation (ASC) architecture for program execution, Leap+Verify decomposes training into three dynamically detected regimes (chaotic, transition, stable) using activation-space cosine similarity as a real-time Lyapunov proxy signal. Within each regime, analytic weight predictors (momentum, linear, quadratic extrapolation) attempt to forecast model parameters K training steps ahead; predictions are accepted only when validated against a held-out loss criterion. We evaluate Leap+Verify on GPT-2 124M and Qwen 2.5-1.5B trained on WikiText-103 across five random seeds, sweeping prediction depth K in {5, 10, 25, 50, 75, 100}. Momentum-based prediction (Adam moment extrapolation) fails catastrophically at both scales, with predicted losses exceeding actuals by 100-10,000x -- a universal norm explosion in optimizer-state extrapolation. Finite-difference predictors (linear, quadratic) succeed where momentum fails: at 124M, they achieve 24% strict acceptance at K=5 in stable regimes; at 1.5B, they achieve 37% strict acceptance in transition regimes. The scale-dependent finding is in regime distribution: GPT-2 124M spends 34% of training in stable regime, while Qwen 1.5B spends 64% in chaotic regime and reaches stable in only 0-2 of 40 checkpoints. Larger models are more predictable when predictable, but less often predictable -- the practical bottleneck shifts from predictor accuracy to regime availability. Cross-seed results are highly consistent (less than 1% validation loss variance), and the three-regime framework produces identical phase boundaries (plus or minus 50 steps) across seeds.

