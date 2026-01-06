---
layout: default
title: TalkPhoto: A Versatile Training-Free Conversational Assistant for Intelligent Image Editing
---

# TalkPhoto: A Versatile Training-Free Conversational Assistant for Intelligent Image Editing
**arXiv**：[2601.01915v1](https://arxiv.org/abs/2601.01915) · [PDF](https://arxiv.org/pdf/2601.01915.pdf)  
**作者**：Yujie Hu, Zecheng Tang, Xu Jiang, Weiqi Li, Jian Zhang  

**一句话要点**：提出TalkPhoto，一种无需训练的对话式图像编辑框架，通过调用现有方法实现精确编辑。

**关键词**：图像编辑, 对话式交互, 无需训练框架, 多模态大语言模型, 提示工程

## 3 点简述
- 现有基于指令的图像编辑方法依赖多指令数据集训练，耗时且效果有限。
- TalkPhoto使用提示模板引导开源LLM分析用户需求，分层调用高级编辑方法，无需额外训练。
- 实验表明，该方法在多种编辑任务中实现更准确调用和更高编辑质量。

## 摘要（原文）

> Thanks to the powerful language comprehension capabilities of Large Language Models (LLMs), existing instruction-based image editing methods have introduced Multimodal Large Language Models (MLLMs) to promote information exchange between instructions and images, ensuring the controllability and flexibility of image editing. However, these frameworks often build a multi-instruction dataset to train the model to handle multiple editing tasks, which is not only time-consuming and labor-intensive but also fails to achieve satisfactory results. In this paper, we present TalkPhoto, a versatile training-free image editing framework that facilitates precise image manipulation through conversational interaction. We instruct the open-source LLM with a specially designed prompt template to analyze user needs after receiving instructions and hierarchically invoke existing advanced editing methods, all without additional training. Moreover, we implement a plug-and-play and efficient invocation of image editing methods, allowing complex and unseen editing tasks to be integrated into the current framework, achieving stable and high-quality editing results. Extensive experiments demonstrate that our method not only provides more accurate invocation with fewer token consumption but also achieves higher editing quality across various image editing tasks.

