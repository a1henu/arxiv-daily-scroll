---
layout: default
title: OmniEarth: A Benchmark for Evaluating Vision-Language Models in Geospatial Tasks
---

# OmniEarth: A Benchmark for Evaluating Vision-Language Models in Geospatial Tasks
**arXiv**：[2603.09471v1](https://arxiv.org/abs/2603.09471) · [PDF](https://arxiv.org/pdf/2603.09471.pdf)  
**作者**：Ronghao Fu, Haoran Liu, Weijie Zhang, Zhiwen Lin, Xiao Yang, Peng Zhang, Bo Yang  

**一句话要点**：提出OmniEarth基准以系统评估遥感视觉语言模型在地球观测任务中的性能

**关键词**：遥感视觉语言模型, 地球观测基准, 多源感知数据, 语义一致性, 盲测协议, 地理空间任务

## 3 点简述
- 核心问题：缺乏系统基准评估遥感视觉语言模型在地球观测场景中的能力
- 方法要点：基于感知、推理和鲁棒性三个维度定义28个细粒度任务，支持多选和开放式问答
- 实验或效果：评估现有模型显示其在复杂地理空间任务中仍存在明显差距

## 摘要（原文）

> Vision-Language Models (VLMs) have demonstrated effective perception and reasoning capabilities on general-domain tasks, leading to growing interest in their application to Earth observation. However, a systematic benchmark for comprehensively evaluating remote sensing vision-language models (RSVLMs) remains lacking. To address this gap, we introduce OmniEarth, a benchmark for evaluating RSVLMs under realistic Earth observation scenarios. OmniEarth organizes tasks along three capability dimensions: perception, reasoning, and robustness. It defines 28 fine-grained tasks covering multi-source sensing data and diverse geospatial contexts. The benchmark supports two task formulations: multiple-choice VQA and open-ended VQA. The latter includes pure text outputs for captioning tasks, bounding box outputs for visual grounding tasks, and mask outputs for segmentation tasks. To reduce linguistic bias and examine whether model predictions rely on visual evidence, OmniEarth adopts a blind test protocol and a quintuple semantic consistency requirement. OmniEarth includes 9,275 carefully quality-controlled images, including proprietary satellite imagery from Jilin-1 (JL-1), along with 44,210 manually verified instructions. We conduct a systematic evaluation of contrastive learning-based models, general closed-source and open-source VLMs, as well as RSVLMs. Results show that existing VLMs still struggle with geospatially complex tasks, revealing clear gaps that need to be addressed for remote sensing applications. OmniEarth is publicly available at https://huggingface.co/datasets/sjeeudd/OmniEarth.

