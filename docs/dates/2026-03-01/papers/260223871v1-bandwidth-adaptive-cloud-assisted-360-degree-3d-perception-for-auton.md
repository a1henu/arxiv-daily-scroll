---
layout: default
title: Bandwidth-adaptive Cloud-Assisted 360-Degree 3D Perception for Autonomous Vehicles
---

# Bandwidth-adaptive Cloud-Assisted 360-Degree 3D Perception for Autonomous Vehicles
**arXiv**：[2602.23871v1](https://arxiv.org/abs/2602.23871) · [PDF](https://arxiv.org/pdf/2602.23871.pdf)  
**作者**：Faisal Hawladera, Rui Meireles, Gamal Elghazaly, Ana Aguiar, Raphaël Frank  

**一句话要点**：提出带宽自适应的云辅助360度3D感知方法，以降低自动驾驶延迟并提升准确性。

**关键词**：自动驾驶感知, 云边协同, Transformer模型, V2X通信, 动态优化算法

## 3 点简述
- 核心问题：自动驾驶在复杂城市环境中，车载计算资源有限导致实时感知延迟。
- 方法要点：利用V2X通信将Transformer模型处理动态分割至云端，结合特征量化和压缩减少网络负载。
- 实验或效果：实验显示延迟降低72%，自适应算法在带宽波动下提升准确性达20%。

## 摘要（原文）

> A key challenge for autonomous driving lies in maintaining real-time situational awareness regarding surrounding obstacles under strict latency constraints. The high processing requirements coupled with limited onboard computational resources can cause delay issues, particularly in complex urban settings. To address this, we propose leveraging Vehicle-to-Everything (V2X) communication to partially offload processing to the cloud, where compute resources are abundant, thus reducing overall latency. Our approach utilizes transformer-based models to fuse multi-camera sensor data into a comprehensive Bird's-Eye View (BEV) representation, enabling accurate 360-degree 3D object detection. The computation is dynamically split between the vehicle and the cloud based on the number of layers processed locally and the quantization level of the features. To further reduce network load, we apply feature vector clipping and compression prior to transmission. In a real-world experimental evaluation, our hybrid strategy achieved a 72 \% reduction in end-to-end latency compared to a traditional onboard solution. To adapt to fluctuating network conditions, we introduce a dynamic optimization algorithm that selects the split point and quantization level to maximize detection accuracy while satisfying real-time latency constraints. Trace-based evaluation under realistic bandwidth variability shows that this adaptive approach improves accuracy by up to 20 \% over static parameterization with the same latency performance.

