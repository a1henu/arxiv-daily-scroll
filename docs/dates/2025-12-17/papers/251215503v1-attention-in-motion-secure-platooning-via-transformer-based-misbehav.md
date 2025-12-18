---
layout: default
title: Attention in Motion: Secure Platooning via Transformer-based Misbehavior Detection
---

# Attention in Motion: Secure Platooning via Transformer-based Misbehavior Detection
**arXiv**：[2512.15503v1](https://arxiv.org/abs/2512.15503) · [PDF](https://arxiv.org/pdf/2512.15503.pdf)  
**作者**：Konstantinos Kalogiannis, Ahmed Mohamed Hussain, Hexu Li, Panos Papadimitratos  

**一句话要点**：提出AIMformer框架，基于Transformer实现车联网编队中的实时异常行为检测

**关键词**：车联网安全, 异常行为检测, Transformer模型, 实时边缘部署, 编队控制

## 3 点简述
- 核心问题：车联网编队中认证车辆注入虚假运动数据，威胁安全与稳定性，传统方法误报率高且难以捕捉时空依赖
- 方法要点：利用多头自注意力机制捕获车辆内时间动态和车辆间空间关联，结合全局位置编码处理编队加入/退出操作
- 实验或效果：在多种控制器、攻击场景和移动性场景下评估，性能优于基线（≥0.93），部署分析显示亚毫秒级推理延迟

## 摘要（原文）

> Vehicular platooning promises transformative improvements in transportation efficiency and safety through the coordination of multi-vehicle formations enabled by Vehicle-to-Everything (V2X) communication. However, the distributed nature of platoon coordination creates security vulnerabilities, allowing authenticated vehicles to inject falsified kinematic data, compromise operational stability, and pose a threat to passenger safety. Traditional misbehaviour detection approaches, which rely on plausibility checks and statistical methods, suffer from high False Positive (FP) rates and cannot capture the complex temporal dependencies inherent in multi-vehicle coordination dynamics. We present Attention In Motion (AIMformer), a transformer-based framework specifically tailored for real-time misbehaviour detection in vehicular platoons with edge deployment capabilities. AIMformer leverages multi-head self-attention mechanisms to simultaneously capture intra-vehicle temporal dynamics and inter-vehicle spatial correlations. It incorporates global positional encoding with vehicle-specific temporal offsets to handle join/exit maneuvers. We propose a Precision-Focused (BCE) loss function that penalizes FPs to meet the requirements of safety-critical vehicular systems. Extensive evaluation across 4 platoon controllers, multiple attack vectors, and diverse mobility scenarios demonstrates superior performance ($\geq$ 0.93) compared to state-of-the-art baseline architectures. A comprehensive deployment analysis utilizing TensorFlow Lite (TFLite), Open Neural Network Exchange (ONNX), and TensorRT achieves sub-millisecond inference latency, making it suitable for real-time operation on resource-constrained edge platforms. Hence, validating AIMformer is viable for both in-vehicle and roadside infrastructure deployment.

