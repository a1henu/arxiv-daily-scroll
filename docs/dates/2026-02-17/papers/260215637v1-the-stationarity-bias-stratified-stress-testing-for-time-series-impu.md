---
layout: default
title: The Stationarity Bias: Stratified Stress-Testing for Time-Series Imputation in Regulated Dynamical Systems
---

# The Stationarity Bias: Stratified Stress-Testing for Time-Series Imputation in Regulated Dynamical Systems
**arXiv**：[2602.15637v1](https://arxiv.org/abs/2602.15637) · [PDF](https://arxiv.org/pdf/2602.15637.pdf)  
**作者**：Amirreza Dolatpour Fathkouhi, Alireza Namazi, Heman Shakeri  

**一句话要点**：提出分层压力测试以解决时间序列插值中的平稳性偏差问题，适用于受调控动态系统。

**关键词**：时间序列插值, 平稳性偏差, 分层压力测试, 动态系统, 形态保真, 机制条件评估

## 3 点简述
- 核心问题：时间序列插值基准存在平稳性偏差，简单方法因主导吸引子而表现虚假优越。
- 方法要点：通过分层压力测试，将评估划分为平稳和瞬态机制，使用真实强制函数进行精确识别。
- 实验或效果：在线性插值在平稳机制高效，深度学习在瞬态机制保持形态保真，支持机制条件模型选择。

## 摘要（原文）

> Time-series imputation benchmarks employ uniform random masking and shape-agnostic metrics (MSE, RMSE), implicitly weighting evaluation by regime prevalence. In systems with a dominant attractor -- homeostatic physiology, nominal industrial operation, stable network traffic -- this creates a systematic \emph{Stationarity Bias}: simple methods appear superior because the benchmark predominantly samples the easy, low-entropy regime where they trivially succeed. We formalize this bias and propose a \emph{Stratified Stress-Test} that partitions evaluation into Stationary and Transient regimes. Using Continuous Glucose Monitoring (CGM) as a testbed -- chosen for its rigorous ground-truth forcing functions (meals, insulin) that enable precise regime identification -- we establish three findings with broad implications:(i)~Stationary Efficiency: Linear interpolation achieves state-of-the-art reconstruction during stable intervals, confirming that complex architectures are computationally wasteful in low-entropy regimes.(ii)~Transient Fidelity: During critical transients (post-prandial peaks, hypoglycemic events), linear methods exhibit drastically degraded morphological fidelity (DTW), disproportionate to their RMSE -- a phenomenon we term the \emph{RMSE Mirage}, where low pointwise error masks the destruction of signal shape.(iii)~Regime-Conditional Model Selection: Deep learning models preserve both pointwise accuracy and morphological integrity during transients, making them essential for safety-critical downstream tasks. We further derive empirical missingness distributions from clinical trials and impose them on complete training data, preventing models from exploiting unrealistically clean observations and encouraging robustness under real-world missingness. This framework generalizes to any regulated system where routine stationarity dominates critical transients.

