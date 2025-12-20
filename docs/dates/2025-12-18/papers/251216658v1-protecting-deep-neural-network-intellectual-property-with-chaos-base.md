---
layout: default
title: Protecting Deep Neural Network Intellectual Property with Chaos-Based White-Box Watermarking
---

# Protecting Deep Neural Network Intellectual Property with Chaos-Based White-Box Watermarking
**arXiv**：[2512.16658v1](https://arxiv.org/abs/2512.16658) · [PDF](https://arxiv.org/pdf/2512.16658.pdf)  
**作者**：Sangeeth B, Serena Nicolazzo, Deepa K., Vinod P  

**一句话要点**：提出基于混沌序列的白盒水印框架以保护深度神经网络知识产权

**关键词**：白盒水印, 混沌序列, 知识产权保护, 深度神经网络, 所有权验证

## 3 点简述
- 核心问题：深度神经网络易被复制或滥用，需有效机制保护模型所有权。
- 方法要点：使用逻辑映射生成混沌序列，嵌入中间层权重，无需修改结构或降低性能。
- 实验或效果：在MNIST和CIFAR-10数据集上验证，水印在微调后仍可检测，精度损失可忽略。

## 摘要（原文）

> The rapid proliferation of deep neural networks (DNNs) across several domains has led to increasing concerns regarding intellectual property (IP) protection and model misuse. Trained DNNs represent valuable assets, often developed through significant investments. However, the ease with which models can be copied, redistributed, or repurposed highlights the urgent need for effective mechanisms to assert and verify model ownership. In this work, we propose an efficient and resilient white-box watermarking framework that embeds ownership information into the internal parameters of a DNN using chaotic sequences. The watermark is generated using a logistic map, a well-known chaotic function, producing a sequence that is sensitive to its initialization parameters. This sequence is injected into the weights of a chosen intermediate layer without requiring structural modifications to the model or degradation in predictive performance. To validate ownership, we introduce a verification process based on a genetic algorithm that recovers the original chaotic parameters by optimizing the similarity between the extracted and regenerated sequences. The effectiveness of the proposed approach is demonstrated through extensive experiments on image classification tasks using MNIST and CIFAR-10 datasets. The results show that the embedded watermark remains detectable after fine-tuning, with negligible loss in model accuracy. In addition to numerical recovery of the watermark, we perform visual analyses using weight density plots and construct activation-based classifiers to distinguish between original, watermarked, and tampered models. Overall, the proposed method offers a flexible and scalable solution for embedding and verifying model ownership in white-box settings well-suited for real-world scenarios where IP protection is critical.

