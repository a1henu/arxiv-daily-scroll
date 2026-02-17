---
layout: default
title: ThermEval: A Structured Benchmark for Evaluation of Vision-Language Models on Thermal Imagery
---

# ThermEval: A Structured Benchmark for Evaluation of Vision-Language Models on Thermal Imagery
**arXiv**：[2602.14989v1](https://arxiv.org/abs/2602.14989) · [PDF](https://arxiv.org/pdf/2602.14989.pdf)  
**作者**：Ayush Shrivastava, Kirtan Gangani, Laksh Jain, Mayank Goel, Nipun Batra  

**一句话要点**：提出ThermEval基准以评估视觉语言模型在热成像上的性能，解决RGB模型在热图像理解上的不足。

**关键词**：热成像视觉语言模型, 温度基础推理, 视觉问答基准, 热图像数据集, 模型泛化评估

## 3 点简述
- 核心问题：视觉语言模型在RGB图像表现良好，但无法泛化到热成像，缺乏温度基础推理能力。
- 方法要点：构建ThermEval-B基准，包含约55,000个热视觉问答对，整合公开数据集和新收集的ThermEval-D数据集。
- 实验或效果：评估25个模型，发现模型在温度推理、色彩映射变换下表现差，仅通过提示或微调有边际提升。

## 摘要（原文）

> Vision language models (VLMs) achieve strong performance on RGB imagery, but they do not generalize to thermal images. Thermal sensing plays a critical role in settings where visible light fails, including nighttime surveillance, search and rescue, autonomous driving, and medical screening. Unlike RGB imagery, thermal images encode physical temperature rather than color or texture, requiring perceptual and reasoning capabilities that existing RGB-centric benchmarks do not evaluate. We introduce ThermEval-B, a structured benchmark of approximately 55,000 thermal visual question answering pairs designed to assess the foundational primitives required for thermal vision language understanding. ThermEval-B integrates public datasets with our newly collected ThermEval-D, the first dataset to provide dense per-pixel temperature maps with semantic body-part annotations across diverse indoor and outdoor environments. Evaluating 25 open-source and closed-source VLMs, we find that models consistently fail at temperature-grounded reasoning, degrade under colormap transformations, and default to language priors or fixed responses, with only marginal gains from prompting or supervised fine-tuning. These results demonstrate that thermal understanding requires dedicated evaluation beyond RGB-centric assumptions, positioning ThermEval as a benchmark to drive progress in thermal vision language modeling.

