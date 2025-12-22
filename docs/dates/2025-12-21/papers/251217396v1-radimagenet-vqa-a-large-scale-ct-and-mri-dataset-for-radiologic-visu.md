---
layout: default
title: RadImageNet-VQA: A Large-Scale CT and MRI Dataset for Radiologic Visual Question Answering
---

# RadImageNet-VQA: A Large-Scale CT and MRI Dataset for Radiologic Visual Question Answering
**arXiv**：[2512.17396v1](https://arxiv.org/abs/2512.17396) · [PDF](https://arxiv.org/pdf/2512.17396.pdf)  
**作者**：Léo Butsanets, Charles Corbière, Julien Khlaut, Pierre Manceron, Corentin Dancette  

**一句话要点**：提出RadImageNet-VQA大规模CT和MRI数据集以推进放射学视觉问答研究

**关键词**：放射学视觉问答, CT和MRI数据集, 病理识别, 大规模标注, 视觉语言模型, 医学图像分析

## 3 点简述
- 现有医学VQA数据集规模小、依赖X射线或插图，易受文本捷径影响
- RadImageNet-VQA提供75万图像和750万问答对，覆盖异常检测、解剖识别和病理识别任务
- 实验显示先进模型在细粒度病理识别上仍困难，且无图像输入时性能接近随机

## 摘要（原文）

> In this work, we introduce RadImageNet-VQA, a large-scale dataset designed to advance radiologic visual question answering (VQA) on CT and MRI exams. Existing medical VQA datasets are limited in scale, dominated by X-ray imaging or biomedical illustrations, and often prone to text-based shortcuts. RadImageNet-VQA is built from expert-curated annotations and provides 750K images paired with 7.5M question-answer samples. It covers three key tasks - abnormality detection, anatomy recognition, and pathology identification - spanning eight anatomical regions and 97 pathology categories, and supports open-ended, closed-ended, and multiple-choice questions. Extensive experiments show that state-of-the-art vision-language models still struggle with fine-grained pathology identification, particularly in open-ended settings and even after fine-tuning. Text-only analysis further reveals that model performance collapses to near-random without image inputs, confirming that RadImageNet-VQA is free from linguistic shortcuts. The full dataset and benchmark are publicly available at https://huggingface.co/datasets/raidium/RadImageNet-VQA.

