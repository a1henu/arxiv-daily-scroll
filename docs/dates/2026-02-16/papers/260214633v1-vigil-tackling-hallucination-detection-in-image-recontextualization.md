---
layout: default
title: VIGIL: Tackling Hallucination Detection in Image Recontextualization
---

# VIGIL: Tackling Hallucination Detection in Image Recontextualization
**arXiv**：[2602.14633v1](https://arxiv.org/abs/2602.14633) · [PDF](https://arxiv.org/pdf/2602.14633.pdf)  
**作者**：Joanna Wojciechowicz, Maria Łubniewska, Jakub Antczak, Justyna Baczyńska, Wojciech Gromski, Wojciech Kozłowski, Maciej Zięba  

**一句话要点**：提出VIGIL基准数据集与框架，以细粒度分类检测多模态图像重上下文化中的幻觉问题。

**关键词**：多模态图像重上下文化, 幻觉检测, 基准数据集, 细粒度分类, 多阶段检测流程, 开源模型集成

## 3 点简述
- 核心问题：现有研究将幻觉视为统一问题，缺乏多模态评估中对幻觉的细粒度分类。
- 方法要点：提出多阶段检测流程，通过专门步骤处理对象级保真度、背景一致性和遗漏检测。
- 实验或效果：通过广泛实验评估，展示开源模型集成的有效性，并公开数据集和代码以促进透明探索。

## 摘要（原文）

> We introduce VIGIL (Visual Inconsistency & Generative In-context Lucidity), the first benchmark dataset and framework providing a fine-grained categorization of hallucinations in the multimodal image recontextualization task for large multimodal models (LMMs). While existing research often treats hallucinations as a uniform issue, our work addresses a significant gap in multimodal evaluation by decomposing these errors into five categories: pasted object hallucinations, background hallucinations, object omission, positional & logical inconsistencies, and physical law violations. To address these complexities, we propose a multi-stage detection pipeline. Our architecture processes recontextualized images through a series of specialized steps targeting object-level fidelity, background consistency, and omission detection, leveraging a coordinated ensemble of open-source models, whose effectiveness is demonstrated through extensive experimental evaluations. Our approach enables a deeper understanding of where the models fail with an explanation; thus, we fill a gap in the field, as no prior methods offer such categorization and decomposition for this task. To promote transparency and further exploration, we openly release VIGIL, along with the detection pipeline and benchmark code, through our GitHub repository: https://github.com/mlubneuskaya/vigil and Data repository: https://huggingface.co/datasets/joannaww/VIGIL.

