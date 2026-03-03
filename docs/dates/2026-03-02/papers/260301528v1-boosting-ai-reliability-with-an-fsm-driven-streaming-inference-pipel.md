---
layout: default
title: Boosting AI Reliability with an FSM-Driven Streaming Inference Pipeline: An Industrial Case
---

# Boosting AI Reliability with an FSM-Driven Streaming Inference Pipeline: An Industrial Case
**arXiv**：[2603.01528v1](https://arxiv.org/abs/2603.01528) · [PDF](https://arxiv.org/pdf/2603.01528.pdf)  
**作者**：Yutian Zhang, Zhongyi Pei, Yi Mao, Chen Wang, Lin Liu, Jianmin Wang  

**一句话要点**：提出基于有限状态机的流式推理管道，以提升工业AI在挖掘机工作量计数中的可靠性。

**关键词**：流式推理, 有限状态机, 工业AI, 目标检测, 鲁棒性增强

## 3 点简述
- 工业AI面临训练数据外场景的鲁棒性不足问题，导致预测偏差和脆弱性。
- 方法结合目标检测模型与有限状态机，通过先验知识引导和修正流式数据上的AI预测。
- 在真实数据集上实验，相比基于手动启发式规则的原始方案，表现出更优性能和更强鲁棒性。

## 摘要（原文）

> The widespread adoption of AI in industry is often hampered by its limited robustness when faced with scenarios absent from training data, leading to prediction bias and vulnerabilities. To address this, we propose a novel streaming inference pipeline that enhances data-driven models by explicitly incorporating prior knowledge. This paper presents the work on an industrial AI application that automatically counts excavator workloads from surveillance videos. Our approach integrates an object detection model with a Finite State Machine (FSM), which encodes knowledge of operational scenarios to guide and correct the AI's predictions on streaming data. In experiments on a real-world dataset of over 7,000 images from 12 site videos, encompassing more than 300 excavator workloads, our method demonstrates superior performance and greater robustness compared to the original solution based on manual heuristic rules. We will release the code at https://github.com/thulab/video-streamling-inference-pipeline.

