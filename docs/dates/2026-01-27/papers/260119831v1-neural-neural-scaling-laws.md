---
layout: default
title: Neural Neural Scaling Laws
---

# Neural Neural Scaling Laws
**arXiv**：[2601.19831v1](https://arxiv.org/abs/2601.19831) · [PDF](https://arxiv.org/pdf/2601.19831.pdf)  
**作者**：Michael Y. Hu, Jane Pan, Ayush Rajesh Jhaveri, Nicholas Lourie, Kyunghyun Cho  

**一句话要点**：提出NeuNeu神经网络，通过时间序列外推预测下游任务缩放规律，避免参数化假设。

**关键词**：缩放定律预测, 时间序列外推, 下游任务性能, 神经网络模型, 零样本泛化

## 3 点简述
- 核心问题：验证困惑度预测下游性能受限，平均损失掩盖信号，参数化模型无法捕捉多样缩放行为。
- 方法要点：NeuNeu结合观察到的准确率轨迹和令牌级验证损失，作为时间序列外推任务学习预测。
- 实验或效果：在66个下游任务上平均绝对误差2.04%，比逻辑缩放定律降低38%，零样本泛化到未见模型和任务。

## 摘要（原文）

> Neural scaling laws predict how language model performance improves with increased compute. While aggregate metrics like validation loss can follow smooth power-law curves, individual downstream tasks exhibit diverse scaling behaviors: some improve monotonically, others plateau, and some even degrade with scale. We argue that predicting downstream performance from validation perplexity suffers from two limitations: averaging token-level losses obscures signal, and no simple parametric family can capture the full spectrum of scaling behaviors. To address this, we propose Neural Neural Scaling Laws (NeuNeu), a neural network that frames scaling law prediction as time-series extrapolation. NeuNeu combines temporal context from observed accuracy trajectories with token-level validation losses, learning to predict future performance without assuming any bottleneck or functional form. Trained entirely on open-source model checkpoints from HuggingFace, NeuNeu achieves 2.04% mean absolute error in predicting model accuracy on 66 downstream tasks -- a 38% reduction compared to logistic scaling laws (3.29% MAE). Furthermore, NeuNeu generalizes zero-shot to unseen model families, parameter counts, and downstream tasks. Our work suggests that predicting downstream scaling laws directly from data outperforms parametric alternatives.

