---
layout: default
title: Collaborative Edge-to-Server Inference for Vision-Language Models
---

# Collaborative Edge-to-Server Inference for Vision-Language Models
**arXiv**：[2512.16349v1](https://arxiv.org/abs/2512.16349) · [PDF](https://arxiv.org/pdf/2512.16349.pdf)  
**作者**：Soochang Song, Yongjune Kim  

**一句话要点**：提出协作式边端到服务器推理框架，以降低视觉语言模型通信成本并保持精度

**关键词**：视觉语言模型, 边端计算, 协作推理, 通信优化, 兴趣区域检测, 最小熵置信度

## 3 点简述
- 核心问题：边端设备传输全局图像至服务器时，分辨率调整导致细节丢失，影响推理精度
- 方法要点：服务器先推理全局图像，基于注意力识别兴趣区域，通过最小熵置信度决定是否请求边端传输局部图像进行细化
- 实验或效果：在多种视觉语言模型架构上验证，显著减少通信成本，同时维持推理精度

## 摘要（原文）

> We propose a collaborative edge-to-server inference framework for vision-language models (VLMs) that reduces the communication cost while maintaining inference accuracy. In typical deployments, visual data captured at edge devices (clients) is transmitted to the server for VLM inference. However, resizing the original image (global image) to match the vision encoder's input resolution often discards fine-grained details, leading to accuracy degradation. To overcome this limitation, we design a two-stage framework. In the first stage, the server performs inference on the global image and identifies a region of interest (RoI) using the VLM's internal attention. The min-entropy of the output tokens is then computed as a confidence measure to determine whether retransmission is required. If the min-entropy exceeds a predefined threshold, the server requests the edge device to send a detail-preserved local image of the RoI. The server then refines its inference by jointly leveraging the global and local images. This selective retransmission strategy ensures that only essential visual content is transmitted. Experiments across multiple VLM architectures show that the proposed framework significantly reduces communication cost while maintaining inference accuracy.

