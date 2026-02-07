---
layout: default
title: A Hybrid Data-Driven Algorithm for Real-Time Friction Force Estimation in Hydraulic Cylinders
---

# A Hybrid Data-Driven Algorithm for Real-Time Friction Force Estimation in Hydraulic Cylinders
**arXiv**：[2602.05967v1](https://arxiv.org/abs/2602.05967) · [PDF](https://arxiv.org/pdf/2602.05967.pdf)  
**作者**：Mohamad Amin Jamshidi, Mehrbod Zarifi, Zolfa Anvari, Hamed Ghafarirad, Mohammad Zareinejad  

**一句话要点**：提出基于LSTM与随机森林的混合算法，用于液压缸实时摩擦力估计，以解决传统模型适应性差与计算效率低的问题。

**关键词**：液压系统, 摩擦力估计, 长短期记忆网络, 随机森林, 实时控制, 混合算法

## 3 点简述
- 液压缸摩擦力建模精度不足，传统分析模型如LuGre模型难以动态适应多变工况。
- 结合LSTM网络与随机森林，通过特征检测与估计过程，实现非线性摩擦力估计。
- 实验验证模型误差低于10%，计算成本1.51毫秒/次，适用于实时应用，性能优于LuGre模型。

## 摘要（原文）

> Hydraulic systems are widely utilized in industrial applications due to their high force generation, precise control, and ability to function in harsh environments. Hydraulic cylinders, as actuators in these systems, apply force and position through the displacement of hydraulic fluid, but their operation is significantly influenced by friction force. Achieving precision in hydraulic cylinders requires an accurate friction model under various operating conditions. Existing analytical models, often derived from experimental tests, necessitate the identification or estimation of influencing factors but are limited in adaptability and computational efficiency. This research introduces a data-driven, hybrid algorithm based on Long Short-Term Memory (LSTM) networks and Random Forests for nonlinear friction force estimation. The algorithm effectively combines feature detection and estimation processes using training data acquired from an experimental hydraulic test setup. It achieves a consistent and stable model error of less than 10% across diverse operating conditions and external load variations, ensuring robust performance in complex situations. The computational cost of the algorithm is 1.51 milliseconds per estimation, making it suitable for real-time applications. The proposed method addresses the limitations of analytical models by delivering high precision and computational efficiency. The algorithm's performance is validated through detailed analysis and experimental results, including direct comparisons with the LuGre model. The comparison highlights that while the LuGre model offers a theoretical foundation for friction modeling, its performance is limited by its inability to dynamically adjust to varying operational conditions of the hydraulic cylinder, further emphasizing the advantages of the proposed hybrid approach in real-time applications.

