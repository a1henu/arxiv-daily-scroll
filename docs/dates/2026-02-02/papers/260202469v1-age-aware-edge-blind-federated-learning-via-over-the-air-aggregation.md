---
layout: default
title: Age-Aware Edge-Blind Federated Learning via Over-the-Air Aggregation
---

# Age-Aware Edge-Blind Federated Learning via Over-the-Air Aggregation
**arXiv**：[2602.02469v1](https://arxiv.org/abs/2602.02469) · [PDF](https://arxiv.org/pdf/2602.02469.pdf)  
**作者**：Ahmed M. Elshazly, Ahmed Arafa  

**一句话要点**：提出基于年龄感知边缘盲过空中聚合的联邦学习方法，以解决无线衰落信道下模型更新传输的延迟与噪声问题。

**关键词**：联邦学习, 过空中聚合, 无线通信, 多天线系统, 模型压缩, 信道噪声

## 3 点简述
- 研究无线衰落信道下联邦学习，设备无需信道状态信息，参数服务器利用多天线和最大比合并检测更新。
- 采用AgeTop-k选择模型坐标，确保单OFDM符号传输，减少延迟，平衡压缩误差与信道噪声影响。
- 实验表明，更多天线提升精度与收敛速度，AgeTop-k在良好信道下优于随机选择，最优k值取决于信道条件。

## 摘要（原文）

> We study federated learning (FL) over wireless fading channels where multiple devices simultaneously send their model updates. We propose an efficient \emph{age-aware edge-blind over-the-air FL} approach that does not require channel state information (CSI) at the devices. Instead, the parameter server (PS) uses multiple antennas and applies maximum-ratio combining (MRC) based on its estimated sum of the channel gains to detect the parameter updates. A key challenge is that the number of orthogonal subcarriers is limited; thus, transmitting many parameters requires multiple Orthogonal Frequency Division Multiplexing (OFDM) symbols, which increases latency. To address this, the PS selects only a small subset of model coordinates each round using \emph{AgeTop-\(k\)}, which first picks the largest-magnitude entries and then chooses the \(k\) coordinates with the longest waiting times since they were last selected. This ensures that all selected parameters fit into a single OFDM symbol, reducing latency. We provide a convergence bound that highlights the advantages of using a higher number of antenna array elements and demonstrates a key trade-off: increasing \(k\) decreases compression error at the cost of increasing the effect of channel noise. Experimental results show that (i) more PS antennas greatly improve accuracy and convergence speed; (ii) AgeTop-\(k\) outperforms random selection under relatively good channel conditions; and (iii) the optimum \(k\) depends on the channel, with smaller \(k\) being better in noisy settings.

