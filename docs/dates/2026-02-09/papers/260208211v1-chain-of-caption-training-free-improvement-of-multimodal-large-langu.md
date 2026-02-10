---
layout: default
title: Chain-of-Caption: Training-free improvement of multimodal large language model on referring expression comprehension
---

# Chain-of-Caption: Training-free improvement of multimodal large language model on referring expression comprehension
**arXiv**：[2602.08211v1](https://arxiv.org/abs/2602.08211) · [PDF](https://arxiv.org/pdf/2602.08211.pdf)  
**作者**：Yik Lung Pang, Changjae Oh  

**一句话要点**：提出Chain-of-Caption框架，通过无训练方式提升多模态大语言模型在指代表达理解任务上的性能。

**关键词**：指代表达理解, 多模态大语言模型, 无训练框架, 上下文增强, 视觉定位

## 3 点简述
- 核心问题：指代表达理解任务中，多模态大语言模型需精确定位图像中文本描述的对象。
- 方法要点：分析视觉和文本上下文工具对模型的影响，提出无训练框架Chain-of-Caption，结合多种上下文提升性能。
- 实验或效果：在RefCOCO等数据集上，框架在多种IoU阈值下比基线模型提升5%至30%准确率。

## 摘要（原文）

> Given a textual description, the task of referring expression comprehension (REC) involves the localisation of the referred object in an image. Multimodal large language models (MLLMs) have achieved high accuracy on REC benchmarks through scaling up the model size and training data. Moreover, the performance of MLLMs can be further improved using techniques such as Chain-of-Thought and tool use, which provides additional visual or textual context to the model. In this paper, we analyse the effect of various techniques for providing additional visual and textual context via tool use to the MLLM and its effect on the REC task. Furthermore, we propose a training-free framework named Chain-of-Caption to improve the REC performance of MLLMs. We perform experiments on RefCOCO/RefCOCOg/RefCOCO+ and Ref-L4 datasets and show that individual textual or visual context can improve the REC performance without any fine-tuning. By combining multiple contexts, our training-free framework shows between 5% to 30% performance gain over the baseline model on accuracy at various Intersection over Union (IoU) thresholds.

