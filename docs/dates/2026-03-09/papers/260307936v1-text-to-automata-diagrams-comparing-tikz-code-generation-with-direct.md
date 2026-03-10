---
layout: default
title: Text to Automata Diagrams: Comparing TikZ Code Generation with Direct Image Synthesis
---

# Text to Automata Diagrams: Comparing TikZ Code Generation with Direct Image Synthesis
**arXiv**：[2603.07936v1](https://arxiv.org/abs/2603.07936) · [PDF](https://arxiv.org/pdf/2603.07936.pdf)  
**作者**：Ethan Young, Zichun Wang, Aiden Taylor, Chance Jewell, Julian Myers, Satya Sri Rajiteswari Nimmagadda, Anthony White, Aniruddha Maiti, Ananya Jana  

**一句话要点**：比较TikZ代码生成与直接图像合成，以提升学生手绘自动机图表的自动化处理与反馈能力。

**关键词**：自动机图表处理, 视觉语言模型, TikZ代码生成, 自动化教育评估, 学生手绘图像分析

## 3 点简述
- 研究核心问题：评估视觉语言模型和大语言模型处理学生手绘自动机图表的能力，以生成准确文本和数字表示。
- 方法要点：使用扫描的学生手绘图作为输入，通过视觉语言模型生成文本描述，经人工修订后，用大语言模型生成TikZ代码并编译评估。
- 实验或效果：发现直接生成的描述常不准确，人工修正能显著提升质量，为自动化评分和教学材料可访问性提供基础。

## 摘要（原文）

> Diagrams are widely used in teaching computer science courses. They are useful in subjects such as automata and formal languages, data structures, etc. These diagrams, often drawn by students during exams or assignments, vary in structure, layout, and correctness. This study examines whether current vision-language and large language models can process such diagrams and produce accurate textual and digital representations. In this study, scanned student-drawn diagrams are used as input. Then, textual descriptions are generated from these images using a vision-language model. The descriptions are checked and revised by human reviewers to make them accurate. Both the generated and the revised descriptions are then fed to a large language model to generate TikZ code. The resulting diagrams are compiled and then evaluated against the original scanned diagrams. We found descriptions generated directly from images using vision-language models are often incorrect and human correction can substantially improve the quality of vision language model generated descriptions. This research can help computer science education by paving the way for automated grading and feedback and creating more accessible instructional materials.

