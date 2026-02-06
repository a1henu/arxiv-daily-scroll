---
layout: default
title: Pathwise Test-Time Correction for Autoregressive Long Video Generation
---

# Pathwise Test-Time Correction for Autoregressive Long Video Generation
**arXiv**：[2602.05871v1](https://arxiv.org/abs/2602.05871) · [PDF](https://arxiv.org/pdf/2602.05871.pdf)  
**作者**：Xunzhi Xiang, Zixuan Duan, Guiyu Zhang, Haiyu Zhang, Zhe Gao, Junta Wu, Shaofeng Zhang, Tengfei Wang, Qi Fan, Chunchao Guo  

**一句话要点**：提出测试时校正方法以解决自回归长视频生成中的误差累积问题

**关键词**：长视频生成, 自回归模型, 测试时校正, 误差累积, 蒸馏扩散模型, 视频合成

## 3 点简述
- 核心问题：蒸馏自回归扩散模型在长序列生成中因误差累积导致质量下降
- 方法要点：利用初始帧作为稳定锚点，沿采样轨迹校准中间随机状态，无需训练
- 实验或效果：在30秒基准测试中匹配资源密集型方法质量，生成长度扩展且开销可忽略

## 摘要（原文）

> Distilled autoregressive diffusion models facilitate real-time short video synthesis but suffer from severe error accumulation during long-sequence generation. While existing Test-Time Optimization (TTO) methods prove effective for images or short clips, we identify that they fail to mitigate drift in extended sequences due to unstable reward landscapes and the hypersensitivity of distilled parameters. To overcome these limitations, we introduce Test-Time Correction (TTC), a training-free alternative. Specifically, TTC utilizes the initial frame as a stable reference anchor to calibrate intermediate stochastic states along the sampling trajectory. Extensive experiments demonstrate that our method seamlessly integrates with various distilled models, extending generation lengths with negligible overhead while matching the quality of resource-intensive training-based methods on 30-second benchmarks.

