---
layout: default
title: Reservoir Subspace Injection for Online ICA under Top-n Whitening
---

# Reservoir Subspace Injection for Online ICA under Top-n Whitening
**arXiv**：[2603.02178v1](https://arxiv.org/abs/2603.02178) · [PDF](https://arxiv.org/pdf/2603.02178.pdf)  
**作者**：Wenjun Xiao, Yuda Bi, Vince D Calhoun  

**一句话要点**：提出储层子空间注入诊断与控制方法，以解决在线ICA在非线性混合下因top-n白化丢弃注入特征导致的性能瓶颈。

**关键词**：在线独立成分分析, 非线性混合, 储层子空间注入, top-n白化, 性能诊断, 信号分离

## 3 点简述
- 核心问题：在线独立成分分析在非线性混合下，储层扩展注入的特征可能因top-n白化被丢弃，形成性能瓶颈。
- 方法要点：形式化储层子空间注入问题，提出IER、SSO、ρ_x诊断指标，并设计保护控制器以保留通过方向能量。
- 实验效果：在非线性混合下，保护控制器恢复性能至基线0.1dB内，改进在线ICA达1.7dB，并在超高斯基准上实现正SI-SDRsc增益。

## 摘要（原文）

> Reservoir expansion can improve online independent component analysis (ICA) under nonlinear mixing, yet top-$n$ whitening may discard injected features. We formalize this bottleneck as \emph{reservoir subspace injection} (RSI): injected features help only if they enter the retained eigenspace without displacing passthrough directions. RSI diagnostics (IER, SSO, $ρ_x$) identify a failure mode in our top-$n$ setting: stronger injection increases IER but crowds out passthrough energy ($ρ_x: 1.00\!\rightarrow\!0.77$), degrading SI-SDR by up to $2.2$\,dB. A guarded RSI controller preserves passthrough retention and recovers mean performance to within $0.1$\,dB of baseline $1/N$ scaling. With passthrough preserved, RE-OICA improves over vanilla online ICA by $+1.7$\,dB under nonlinear mixing and achieves positive SI-SDR$_{\mathrm{sc}}$ on the tested super-Gaussian benchmark ($+0.6$\,dB).

