---
layout: default
title: Scaling Test-time Inference for Visual Grounding
---

# Scaling Test-time Inference for Visual Grounding
**arXiv**：[2601.13633v1](https://arxiv.org/abs/2601.13633) · [PDF](https://arxiv.org/pdf/2601.13633.pdf)  
**作者**：Guanqi Zhan, Changye Li, Zhijian Liu, Yao Lu, Yi Wu, Song Han, Ligeng Zhu  

**一句话要点**：提出EGM方法，通过扩展测试时计算提升小模型视觉定位能力，以解决大模型部署效率低的问题。

**关键词**：视觉定位, 测试时计算扩展, 小模型优化, 部署效率, 视觉语言模型

## 3 点简述
- 核心问题：小视觉语言模型因语言理解能力不足，在视觉定位任务中落后于大模型，且大模型部署成本高、推理慢。
- 方法要点：引入EGM，通过增加测试时生成令牌数量来扩展小模型的计算，弥补语言能力差距，提升定位精度。
- 实验或效果：在RefCOCO基准上，EGM-Qwen3-VL-8B达到91.4 IoU，比Qwen3-VL-235B快5.9倍，并在新模态定位设置中验证了方法的通用性。

## 摘要（原文）

> Visual grounding is an essential capability of Visual Language Models (VLMs) to understand the real physical world. Previous state-of-the-art grounding visual language models usually have large model sizes, making them heavy for deployment and slow for inference. However, we notice that the sizes of visual encoders are nearly the same for small and large VLMs and the major difference is the sizes of the language models. Small VLMs fall behind larger VLMs in grounding because of the difference in language understanding capability rather than visual information handling. To mitigate the gap, we introduce 'Efficient visual Grounding language Models' (EGM): a method to scale the test-time computation (#generated tokens). Scaling the test-time computation of a small model is deployment-friendly, and yields better end-to-end latency as the cost of each token is much cheaper compared to directly running a large model. On the RefCOCO benchmark, our EGM-Qwen3-VL-8B demonstrates 91.4 IoU with an average of 737ms (5.9x faster) latency while Qwen3-VL-235B demands 4,320ms to achieve 90.5 IoU. To validate our approach's generality, we further set up a new amodal grounding setting that requires the model to predict both the visible and occluded parts of the objects. Experiments show our method can consistently and significantly improve the vanilla grounding and amodal grounding capabilities of small models to be on par with or outperform the larger models, thereby improving the efficiency for visual grounding.

